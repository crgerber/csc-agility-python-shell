from collections import defaultdict
from ConfigParser import RawConfigParser, NoOptionError
from logger import logger as logger
from core.base.enum import Enum

class ConfigINIFile(object):
    def __init__(self, path=None, load=False, caseSensitive=True):
        self.parser = RawConfigParser()
        if caseSensitive:
            self.parser.optionxform = str#options are case sensitive, and not converted to lower case during load
        self.path = path
        self._valuehooks = defaultdict(dict)
        self._valuehooks.update({'default' : defaultdict(dict), 'formatter' : defaultdict(dict)})
        self._mandatorySections = []
        self._mandatoryOptions = defaultdict(list)
        if load:
            self.load()
    
    def load(self, path=None):
        path = path or self.path
        if not path:
            raise RuntimeError('Failed to load configuration file, No path specified')
        self.parser.read(path)
        return self
                
    def mandatory(self, sections):
        self._mandatorySections = [sections] if isinstance(sections, str) else sections
        
    def mandatoryOptions(self, section, options):
        self._mandatoryOptions[section] = [options] if isinstance(options, str) else options
        
    def sections(self):
        return self.parser.sections()
    
    def section(self, section, get_defaults=True):
        actual_options = self.parser.options(section) #actual options set in the config INI file
        all_defaults = self._valuehooks['default'][section].keys() #all options with default values
        options = list(set(actual_options) | set(all_defaults)) #options = union of actual options loaded from file + options with defautls set
        values = [self.get(section, option) for option in options]
        section = dict(zip(options, values))
        return section
    
    def addSection(self, section, save=False):
        self.parser.add_section(section)
        if save:
            self.save()
            
    def removeSection(self, section, save=False):
        self.parser.remove_section(section)
        if save:
            self.save()
    
    def __contains__(self, section):
        return self.parser.has_section(section)
    
    def __getitem__(self, section):
        return self.section(section)
    
    def __setitem__(self, section):
        return self.addSection(section)
    
    def __delitem__(self, section):
        return self.removeSection(section)
        
    def options(self, section):
        return self.parser.options(section)
    
    def get(self, section, option):
        try:
            value = self.parser.get(section, option)
        except NoOptionError:
            value = self.defaultValue(section, option)
            if value is None:
                raise
        return self.formatValue(section, option, value)

    def getint(self, section, option):
        return self.parser.getint(section, option)

    def getfloat(self, section, option):
        return self.parser.getfloat(section, option)

    def hasOption(self, section, option):
        return self.parser.has_option(section, option)
    
    def setOption(self, section, option, value, save=False):
        self.parser.set(section, option, value)
        if save:
            self.save()
    
    def removeOption(self, section, option, save=False):
        self.parser.remove_option(section, option)
        if save:
            self.save()
            
    def _addValuehook(self, hooklabel, func, section=None, options=None):
        if not section:
            section = 'ALL'
        else:
            self._valuehooks[hooklabel].pop('ALL', '')
            
        if not options:
            self._valuehooks[hooklabel][section]['ALL'] = func
        else:
            options = [options] if isinstance(options, str) else options
            self._valuehooks[hooklabel][section].pop('ALL', '')
            for option in options:
                self._valuehooks[hooklabel][section][option] = func
                
    def _applyValuehook(self, hooklabel, section, option, value=None):
#        logger.debug('%s(%s, %s, %s)', hooklabel, section, option, value)
        hooks = self._valuehooks[hooklabel]
        
        if section not in hooks:
            if 'ALL' not in hooks:
                return value
            else:
                section = 'ALL'
        if option not in hooks[section]:
            if 'ALL' not in hooks[section]:
                return value
            else:
                option = 'ALL'
        return hooks[section][option](value)
                
    def formatter(self, func, section=None, options=None):
        '''
        Install a formatter func for <section|ALL>.[<options1>, <option2>, ...|ALL]. func(value) would be returned instead of value
        '''
        self._addValuehook('formatter', func, section, options)
        
    def default(self, value, section=None, options=None):
        '''
        Set a default value for configuration <section|ALL>.[<options1>, <option2>, ...|ALL]
        
        Makes use of the generic value hooks feature. Note that a value hook func should accept a single argument <value>
        We worked around this interface here by defining lambda *args: value, this way the function wouldn not complain about the "dummuy" argument passed to it
        '''
        self._addValuehook('default', lambda *args: value, section, options)
        
    def formatValue(self, section, option, value):
        '''
        Format a value prior to returning to client code, e.g. split comma separated values into a list of strings
        '''
        return self._applyValuehook('formatter', section, option, value)
    
    def defaultValue(self, section, option):
        '''
        Retreive the default value for section.option
        '''
        return self._applyValuehook('default', section, option, None)
                
    def validate(self):
        self.validateMandatorySections()
        for section in self.sections():
            self.validateSection(section)
        
    def validateMandatorySections(self):
        result = [section in self.sections() for section in self._mandatorySections]
        if not all(result):
            missingSections = [self._mandatorySections[idx] for idx, exists in enumerate(result) if not exists]
            raise RuntimeError('Invalid Configuration, missing sections %s'%missingSections)
            
    def validateSection(self, section):
        self.validateMandatoryOptions(section)
        
    def validateMandatoryOptions(self, section):
        result = [option in self.options(section) for option in self._mandatoryOptions[section]]
        if not all(result):
            missingOptions = [self._mandatoryOptions[section][idx] for idx, exists in enumerate(result) if not exists]
            raise RuntimeError('Invalid Configuration, missing configuration options %s in section [%s]'%(missingOptions, section))
        
    def save(self, saveas=None):
        path = saveas or self.path
        with open(path, 'w') as cfgfile:
            self.parser.write(cfgfile)
        
class AgilityShellConfig(ConfigINIFile):
    def __init__(self, path=None):
        ConfigINIFile.__init__(self, path=path, load=True, caseSensitive=True)
        # Note that if the value is present in the config file, it will be in a string format 
        # while a default value hook might be set to a bool, both values would pass by the formatter before return to the client code
        to_bool = lambda v: str(v) == 'True' 
        
        self.mandatory('main')
        self.mandatoryOptions('main', ['host', 'password'])
        self.default('servicemesh', 'main', 'client')
        self.default('environment', 'main', 'environment')
        self.default(8443, 'main', 'port')
        self.default('admin', 'main', 'username')
        self.default('latest', 'main', 'systemversion')
        self.default(True, 'main', 'prefetch')
        self.formatter(to_bool, 'main', 'prefetch')
        self.default('basic', 'main', 'auth')
        self.default(False, 'main', 'use_cookies')
        self.formatter(to_bool, 'main', 'use_cookies')
        self.default(True, 'main', 'connect')
        self.formatter(to_bool, 'main', 'connect')
        self.default(False, 'main', 'reauthenticate')
        self.formatter(to_bool, 'main', 'reauthenticate')
        self.default('v2.0', 'apiversion', 'version')
        self.default('True', 'apiversion', 'compatibility')
        self.formatter(to_bool, 'apiversion', 'compatibility')
        self.default('INFO', 'log', 'level')
        mainSectionNames = filter(lambda sectionName: sectionName.startswith('main'), self.sections())
        if not mainSectionNames:
            raise RuntimeError('Failed to load configuration file, No [main] section')
        self.mainSectionName = mainSectionNames.pop()
        logger.info('Loading Shell Configuration from %s:[%s]', path, self.mainSectionName)
        self.validateSection(self.mainSectionName)
        self.mainSection = self.section(self.mainSectionName)
        
    def getConfig(self, sectionNames=None):
        sectionNames = sectionNames or [self.mainSectionName]
        configDict = {'%s_%s'%(sectionName, k) : v for sectionName in sectionNames for k, v in self.section(sectionName).items()}
        config = Enum(**configDict)
        return config
