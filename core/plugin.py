'''
Created on Nov 15, 2012

@author: dawood
'''
import os
import sys
import imp
from functools import partial, cmp_to_key
from core.base.enum import Enum
from core.proxy.hook import Hook
from core.pyworx import pythonpath
import traceback
import configparser
import logger
from core.config.configuration import ConfigINIFile
logger = logger.getLogger(__name__)

class PluginConfigFile(ConfigINIFile):
    CONF_MAIN_MODULE = 'mainmodule'
    CONF_MAIN_CLASS = 'mainclass'
    CONF_LOCATION = 'location'
    CONF_LIB_PATHS = 'libpaths'
    CONF_EXTLIB_PATHS = 'extlibpaths'
    CONF_DEPENDENCY = 'dependency'
    CONF_ENABLED = 'enabled'
    CONF_SETUP = 'setup'
    CONF_SYSTEM_SETUP_DONE = 'SYSTEM_setup_successful'
    CONF_META_SECTION_NAME = 'feature_section_name'
    
    MANADATORY_CONF = [CONF_MAIN_MODULE, CONF_LOCATION]
    OPTINOAL_CONF = [CONF_LIB_PATHS, CONF_EXTLIB_PATHS, CONF_DEPENDENCY, CONF_SETUP]
    
    def __init__(self, path):
        ConfigINIFile.__init__(self, path=path, load=True, caseSensitive=True)
        self.load()
        configSectionNames = self.sections()
        self.featureSectionNames = [sectionName for sectionName in configSectionNames if sectionName.startswith('feature')]
        multivalueKeys = [self.CONF_LIB_PATHS, self.CONF_EXTLIB_PATHS, self.CONF_DEPENDENCY]
        for section in self.featureSectionNames:
            self.mandatoryOptions(section, options=self.MANADATORY_CONF)
            self.validateSection(section)
            self.formatter(lambda val: [v.strip() for v in val.split(',')] if val else [], section=section, options=multivalueKeys)
            
    def getFeatureSections(self):
        addName = lambda section, sectionMap: sectionMap.update([(self.CONF_META_SECTION_NAME, section)]) or sectionMap
        featureSections = [addName(section, self.section(section)) for section in self.featureSectionNames]
        return featureSections
        
class PluginLoadError(RuntimeError):
    def __init__(self, pluginpath, msg, *args):
        self.pluginpath = pluginpath
        defaultmsgDetails = (' Details: %s'%str(args)) if args else ''
        defaultmsg = 'Error loading plugin.%s'%defaultmsgDetails
        self.msg = (msg%args) if msg else defaultmsg
        self.args = args
        
    def __repr__(self):
        _repr = '''%(errortype)s
        %(pluginpath)s
        %(errormsg)s
        '''
        return _repr%dict(errortype=type(self), pluginpath=self.pluginpath, errormsg=self.msg)
    
    __str__ = __repr__
    
class PluginConfigError(PluginLoadError):
    def __init__(self, pluginpath, msg, *args):
        PluginLoadError.__init__(self, pluginpath, msg, *args)
    

class AgilityShellHook(object):
    '''
    base plugin class
    '''
    def __init__(self, agility):
        '''
        Constructor
        '''
        self._agility = agility    
        
def validateDependency(pluginpath, pluginlocation, allconfig):
    allfeatures = set([cfg[PluginConfigFile.CONF_LOCATION] for cfg in list(allconfig.values())])
    pluginfeature = (pluginpath, pluginlocation)
    cfg = allconfig[pluginfeature]
    dependencyList = cfg[PluginConfigFile.CONF_DEPENDENCY]
    #normal loop chosen over more compact iteration forms for verbose logs
    for dependency in dependencyList:
        if dependency not in allfeatures:
            raise PluginLoadError(pluginpath, 'Missing dependency [%s] for plugin feature [%s]', dependency, pluginlocation)
    
def loadPlugin(fullpath, config):
    #add plugin fullpath to syspath
    pythonpath.addPath(fullpath)
    
    #add plugin lib fullpath to syspath if any
    if PluginConfigFile.CONF_LIB_PATHS in config:
        libpaths = config[PluginConfigFile.CONF_LIB_PATHS]
        if not isinstance(libpaths, (list, tuple)):
            libpaths = [libpaths]
        pythonpath.addPaths(libpaths, basedir=fullpath)
        logger.debug("basedir:=%s" % str(fullpath))
        logger.debug("libpaths:=%s" % str(libpaths))
        
    #add plugin lib fullpath to syspath if any
    if PluginConfigFile.CONF_EXTLIB_PATHS in config:
        extlibpaths = config[PluginConfigFile.CONF_EXTLIB_PATHS]
        if not isinstance(extlibpaths, (list, tuple)):
            extlibpaths = [extlibpaths]
        #expand real paths
        logger.debug('Adding ext libpaths: %s to sys.path', extlibpaths)
        pythonpath.addPaths(extlibpaths)#slice assignment expands the list within the LHS
    filehandle = None
    mainmodule = None
    mainclass = None
    moduleinterface = []
    try:
        if PluginConfigFile.CONF_SETUP in config:
            setupscript = config[PluginConfigFile.CONF_SETUP]
            if setupscript and not config.get(PluginConfigFile.CONF_SYSTEM_SETUP_DONE, False):                
                if runSetupScript(os.path.join(fullpath, setupscript)):
                    configpath = os.path.join(fullpath, 'plugin.cfg')
                    configfile = PluginConfigFile(configpath)
                    configfile.setOption(config[configfile.CONF_META_SECTION_NAME], configfile.CONF_SYSTEM_SETUP_DONE, 'True', save=True)
                
        filehandle, pathname, description = imp.find_module(config[PluginConfigFile.CONF_MAIN_MODULE])
        
        logger.debug("name:=%s" % str(config[PluginConfigFile.CONF_MAIN_MODULE]))
        logger.debug("file:=%s" % str(filehandle))
        logger.debug("filename:=%s" % pathname)
        logger.debug("description:=%s" % str(description))
        
        if not filehandle:
            raise ImportError()
        mainmodule = imp.load_module(config[PluginConfigFile.CONF_MAIN_MODULE], filehandle, pathname, description)
        if PluginConfigFile.CONF_MAIN_CLASS in config:
            mainclass = getattr(mainmodule, config[PluginConfigFile.CONF_MAIN_CLASS], None)
            if not mainclass:
                raise ImportError('Failed to load main class [%s] from plugin main module [%s]'%(config[PluginConfigFile.CONF_MAIN_CLASS], config[PluginConfigFile.CONF_MAIN_MODULE]))
        else:
            moduleinterface = getattr(mainmodule, '__all__', None)
            if not moduleinterface:
                raise ImportError('Plugin has to declare a main class, or plugin module has to specify a public interface using __all__')
             
    except ImportError as ex:
        logger.error(traceback.format_exc())
        raise PluginLoadError(fullpath, 'Failed to load plugin feature [%s]', config[PluginConfigFile.CONF_LOCATION])
    except AttributeError as ex:
        logger.error(traceback.format_exc())
        raise PluginLoadError(fullpath, 'Failed to load plugin feature [%s]', config[PluginConfigFile.CONF_LOCATION])
    finally:
        if filehandle:
            filehandle.close()
    return mainmodule, mainclass, moduleinterface, config[PluginConfigFile.CONF_LOCATION]

def runSetupScript(path):
    logger.info('Executing plugin setup script [%s]', path)
    cwd = os.path.realpath(os.curdir)#keep current value
    parentDir = os.path.dirname(path)
    scriptFile = os.path.basename(path)
    os.chdir(parentDir)
    result = os.system('python %s install'%scriptFile)
    os.chdir(cwd)#restore current work directory
    return 0 == result
    
def resolveDependency(cfg, othercfg):
    '''
    advanced compare function for sorting plugin list before loading
    must do the compare logic both ways i.e if a depends on b, then b < a, and if b is a dependency of a, then b > a
     
    cmp(location) = [-1 | 0 | 1]
    cmp(dependency) = [-1 | 0 | 1]
    basic truth table proves that simple addition sorts naturally
    ---------------------------------
    location    dependency    result
    ---------------------------------
    -1            -1(*2)        -2(=-3) => natural case, plugin1 location comes before plugin2, dependency plugin1->plugin2 is naturally resolved
    ---------------------------------
    -1            0             -1      => plugin1 should be loaded first, according to location order
    ---------------------------------
    -1            1(*2)          0(=1)  => if plugin1 is parent of plugin2 then ERROR (parent can't depend on child) else dependency should prevail
    ---------------------------------
    0             -1(*2)        -1(-2)  => N/A, ERROR (location conflict)
    ---------------------------------
    0             0              0      => N/A, ERROR (location conflict)
    ---------------------------------
    0             1(*2)          1(=2)  => N/A, ERROR (location conflict)
    ---------------------------------
    1             -1(*2)         0(=-1) => if plugin2 is parent of plugin1 then ERROR (parent can't depend on child) else dependency should prevail
    ---------------------------------
    1             0              1      => location order prevails
    ---------------------------------
    1             1(*2)          2(=3)  => natural case, plugin2 location comes after plugin1, dependency plugin1->plugin2 is naturally resolved
    ---------------------------------
    
    Summary, simply add the two values and checking on error cases should serve the purpose
    '''
    
    #applying basic dependency sorting, by location, e.g.: [a.tools', 'a.tools.ssh', 'a.tools.ssh.ssh2'] to avoid overwriting hooks while loading plugins
    
    locationOrder = 0
    #print("cfgValues:=%s\n\n" % str(cfg))
    
    if  cfg[0][1] < othercfg[0][1] :
        #print("thisLocation(%s) is less than otherLocation(%s)" % (str(cfg[0][1]), str(othercfg[0][1])))
        locationOrder = -1
    elif cfg[0][1] == othercfg[0][1] :
        #print("thisLocation(%s) is equal to otherLocation(%s)" % (str(cfg[0][1]), str(othercfg[0][1])))
        locationOrder = 0
    elif cfg[0][1] > othercfg[0][1] :
        #print("thisLocation(%s) is greater than otherLocation(%s)" % (str(cfg[0][1]), str(othercfg[0][1])))
        locationOrder = 1 
    
    if locationOrder == 0:
        raise ValueError('location conflict [%s]' % cfg[0][1])

    thisDependency = []
    if PluginConfigFile.CONF_DEPENDENCY in cfg[1] and cfg[1][PluginConfigFile.CONF_DEPENDENCY] :
        thisDependency = cfg[1][PluginConfigFile.CONF_DEPENDENCY]
        #print("cfgDependency:=%s" % str(thisDependency))
        
    otherDependency = []
    if PluginConfigFile.CONF_DEPENDENCY in othercfg[1] and othercfg[1][PluginConfigFile.CONF_DEPENDENCY] :
        otherDependency = othercfg[1][PluginConfigFile.CONF_DEPENDENCY]
        #print("oCfgDependency:=%s" % str(otherDependency))

    dependencyOrder = 0;
    if othercfg[0][1] in thisDependency :   
        dependencyOrder = 1 
    elif cfg[0][1] in otherDependency :
        dependencyOrder = -1 
        
    combinedOrder = locationOrder + (2*dependencyOrder)#multiplying by 2 simplifies logic, refer to truth table above
    #print("\n\nCombinedOrder:=%s\n\n" % str(combinedOrder))
    
    parent = '.'.join(cfg[0][1].split('.')[:-1])
    otherparent = '.'.join(othercfg[0][1].split('.')[:-1])
    
    if combinedOrder == 1 and otherparent.startswith(cfg[0][1]):#parent node can't depend on child node, or else internal nodes might be overwritten by dummy hook links
        raise ValueError('invalid dependency, plugin [%s] can not depend on plugin [%s], consider configuring a different "location"'%(cfg[0][1], othercfg[0][1]))
    
    if combinedOrder == -1 and parent.startswith(othercfg[0][1]):#parent node can't depend on child node, or else internal nodes might be overwritten by dummy hook links
        raise ValueError('invalid dependency, plugin [%s] can not depend on plugin [%s], consider configuring a different "location"'%(othercfg[0][1], cfg[0][1]))

    return 1 if combinedOrder > 0 else -1 if combinedOrder < 0 else 0#adhere to cmp interface of returning -1 or 0 or 1
        

def prioritizePlugins(allconfig):
    '''
    sort plugins before loading
    
    basic sorting criteria is location natural order
    will try as well to resolve plugin dependency and update the order for the imports in the plugin module to succeed
    
    @param allconfig: map of {plugin full path -> config}
    @return: ordered list of pairs (plugin full path, config)
    '''
    # prioritizedPlugins = sorted(list(allconfig.items()), key=lambda pair: pair[1], cmp=resolveDependency)
    prioritizedPlugins = sorted(list(allconfig.items()), key=cmp_to_key(resolveDependency))
    return prioritizedPlugins

def loadPlugins(agility, rootpath, plugindir='plugins'):
    isNotHidden = lambda d: not d.startswith('.')
    pluginspath = os.path.join(rootpath, plugindir)
    logger.info('Loading agility shell plugins from [%s]', pluginspath)
    allconfig = {}
    #pre-load all plugins config
    isDir = lambda relpath: isNotHidden(relpath) and os.path.isdir(os.path.join(pluginspath, relpath))
    for plugin in filter(isDir, os.listdir(pluginspath)):
        pluginpath = os.path.join(pluginspath, plugin)
        try:
            configpath = os.path.join(pluginpath, 'plugin.cfg')
            configfile = PluginConfigFile(configpath)
            configSections = configfile.getFeatureSections()
        except Exception as ex:
            logger.error(ex)
            continue
        else:
            for config in configSections:
                if config.get(PluginConfigFile.CONF_ENABLED, 'true').lower() != 'true':
                    continue
                logger.debug('Config: %s'%config)
                #print('Config: %s'%config)
                
                #using tuple (pluginpath, pluginlocation) as key to enable multiple locations per plugin
                allconfig[(pluginpath, config[PluginConfigFile.CONF_LOCATION])] = config
    
    prioritizedPlugins = prioritizePlugins(allconfig)
    for pluginfeature, cfg in prioritizedPlugins:
        pluginpath, pluginlocation = pluginfeature
        
        #print("PluginFeature:=%s" % str(pluginfeature))
        #print("PluginPath:=%s" % pluginpath)
        #print("PluginLocation:=%s" % pluginlocation)
        
        try:
            if PluginConfigFile.CONF_DEPENDENCY in cfg and cfg[PluginConfigFile.CONF_DEPENDENCY]:
                validateDependency(pluginpath, pluginlocation, allconfig)
            agility.cfg.plugins.all[pluginlocation] = cfg
            pluginmodule, pluginclass, moduleinterface, treelocation = loadPlugin(pluginpath, cfg)
            treelocation, cfg = installPlugin(agility, pluginpath, pluginmodule, pluginclass, moduleinterface, treelocation, cfg)
        except Exception as ex:
            logger.error(traceback.format_exc(ex))
            agility.cfg.plugins.failed.add(pluginlocation)
            continue
        
    return agility.cfg.plugins.loaded, agility.cfg.plugins.failed
    
def installPlugin(agility, pluginpath, pluginmodule, pluginclass, moduleinterface, treelocation, cfg):
    logger.info('Installing plugin feature [%s] from [%s]', treelocation, pluginpath)

    if pluginclass:
        logger.debug('Loaded plugin class [%s.%s] for location [%s]', pluginmodule.__name__, pluginclass.__name__, treelocation)
    else:
        logger.debug('Loaded plugin module [%s] for location [%s]', pluginmodule.__name__, treelocation)
        
    treenodes = treelocation.split('.')
    parent = agility
    for treenode in treenodes[1:-1]:#a.[tools.connectors].ssh
        hook = getattr(parent, treenode, None)
        if not hook:
            hook = Hook()
            setattr(parent, treenode, hook)
        parent = hook
    #now the there exists a path to the location, e.g. a.tools.ssh.ssh2, transplant the plugin class leaf into the tree
    if pluginclass:
        setattr(parent, treenodes[-1], pluginclass(agility))
    else:
        pluginHook = Hook()
        [setattr(pluginHook, attrname, getattr(pluginmodule, attrname)) for attrname in moduleinterface]#expose module public interface "__all__" under the new hook
        setattr(parent, treenodes[-1], pluginHook)#plugin end point
    cfg['plugin_path'] = pluginpath
    agility.cfg.plugins.loaded.add(treelocation)
    agility.cfg.plugins.all[treelocation] = cfg
    logger.info('Successfully installed plugin feature [%s] from %s', treelocation, pluginpath)
    return treelocation, cfg

def reloadPluginFeature(agility, treelocation):
    cfg = agility.cfg.plugins.all[treelocation]
    pluginpath = cfg['plugin_path']
    try:
        pluginmodule, pluginclass, moduleinterface, treelocation = loadPlugin(pluginpath, cfg)
        treelocation, cfg = installPlugin(agility, pluginpath, pluginmodule, pluginclass, moduleinterface, treelocation, cfg)
    except PluginLoadError as ex:
        logger.error(ex)
        agility.cfg.plugins.loaded.discard(treelocation)
        agility.cfg.plugins.failed.add(treelocation)
        
    
