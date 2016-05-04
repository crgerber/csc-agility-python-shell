'''
Created on Apr 17, 2013

@author: dawood
'''
import os
import urllib2
from itertools import chain
import re
from lxml import etree
import ssl
import sys
#sys.path.append('/Users/dawood/Documents/workspace/agilitypythonshell/lib/beautifulsoup4-4.1.3/')
sys.path.append('/Users/cgerber/python3-lib/beautifulsoup4-4.4.1/')
from bs4 import BeautifulSoup
from core.restclient.responseparser.ParserLxml import xml2d
from core.pyworx.text import isValidPythonSymbol, validPythonSymbol
from agilityinit import getConfiguration
from core.agility import getModel

agilitymodel = getModel()
configuration = getConfiguration()
ssl._create_default_https_context = ssl._create_unverified_context

CDATA_KEY = '__CDATA__'
PYTHON = 'python'
RUBY = 'ruby'
LANG = configuration.get(section='main', option='lang')
HOST = configuration.get(section='main', option='host')
CODE_FILE_EXTENSION = '.py' if LANG == PYTHON else '.rb' 

ALL_MODULES = set()
ALL_CLASSES = set()
ALL_ENUMS = set()
MODULES_QUEUE = set()
REJECTED_SPECS = set()

def getAllClassesDocsUrls(host):
    allclassesIndex = urllib2.urlopen(url="https://%s:8443/javadoc/scripting/allclasses-frame.html"%host).read()
    allclassesIndexSoup = BeautifulSoup(allclassesIndex, 'html')
    
    allclassesUrls = allclassesIndexSoup.find_all('a')
    return map(lambda link: 'https://%s:8443/javadoc/scripting/%s'%(host, link.get('href')), allclassesUrls)

def getClassDocUrl(host, className):
    urlTemplate = "https://%(host)s:8443/javadoc/scripting/com/servicemesh/agility/api/%(className)s.html"
    return urlTemplate%{'host' : host, 'className' : className}
    
def extractClassSpec(classDocUrl, className=None, asText=False):
    classDoc = urllib2.urlopen(url=classDocUrl).read()
    classDocSoup = BeautifulSoup(classDoc, 'html')
    print("Downloading spec: %s" % classDocUrl)
    dct = extractComplexTypeFromHTML(classDocSoup, asText) or extractSimpleTypeEnumFromHTML(classDocSoup, asText)
    if dct is None:
        REJECTED_SPECS.add(classDocUrl)
    return dct

def extractComplexTypeFromHTML(classDocSoup, asText=False):
    complexType = classDocSoup.find_all('pre', text=re.compile('complexType'))#list of soup objects
    if len(complexType) != 1:
        return '' if asText else {}
    return complexType[0].text if asText else processComplexType(complexType)
    
def processComplexType(complexTypeSoup):    
    complexType = complexTypeSoup[0].text
    node = etree.XML(complexType)
    dct = xml2d(node, loadAttrs=True)
    return dct

def extractSimpleTypeEnumFromHTML(classDocSoup, asText=False):
    simpleType = classDocSoup.find_all('pre', text=re.compile('simpleType'))#list of soup objects
    if len(simpleType) != 1:
        print('Warning: could not parse file')
        return None
    return simpleType[0].text if asText else processSimpleType(simpleType)

def processSimpleType(simpleTypeSoup):
    simpleType = simpleTypeSoup[0].text
    node = etree.XML(simpleType)
    dct = xml2d(node, loadAttrs=True)
    enumName = dct['simpleType']['name']
    if enumName in ALL_MODULES:
        return {}
    restriction = dct['simpleType']['restriction']
    native, baseType = extractType(restriction['base'])
    assert native
    enumeration = restriction.get('enumeration', None)
    assert enumeration is not None
    enumValues = [entry['value'] for entry in enumeration]
    dirname = rootDirName()
    filepath = os.path.join(dirname, enumName + CODE_FILE_EXTENSION)
    print('Writing file: %s'%filepath)
    enumMap = dict(zip(enumValues, enumValues))
    code = getSimpleTypeCodePython(enumName, enumMap) if LANG == PYTHON else getSimpleTypeCodeRuby(enumName, enumMap)
    with open(filepath, 'w') as classFile:
        classFile.write(code)
    ALL_MODULES.add(enumName)
    ALL_ENUMS.add(enumName)
#    with open(os.path.join(dirname, 'base', '__init__.py'), 'w') as packageInitFile:
#        packageInitFile.write('__all__ = %s'%list(ALL_MODULES))   
#    print 'agilitymodel __all__ = %s'%list(ALL_MODULES)
    return {}


def getSimpleTypeCodePython(enumName, enumMap):
    ENUM_TEMPLATE = '''
from core.base.enum import Enum

%(Clazz)s = Enum(**%(enumMap)s)
'''
    return ENUM_TEMPLATE%{'Clazz' : enumName, 'enumMap' : enumMap}

def getSimpleTypeCodeRuby(enumName, enumMap):
    ENUM_TEMPLATE = '''
class %(Clazz)s
  def initialize()
    %(selfAttrs)s
  end
  %(attr_readers)s
end                    
    '''
    enum_context = {}
    enum_context['Clazz'] = enumName
    enum_context['selfAttrs']  = ('\n%s'%(AgilityType.INDENT*2)).join(["@%s = '%s'"%(key, val) for key, val in enumMap.items()])
    enum_context['attr_readers'] = ('\n%s'%(AgilityType.INDENT)).join('attr_reader :%s'%key for key in enumMap.keys())
    return ENUM_TEMPLATE%enum_context

def processClassSpec(specDict, asText = False):
    if not specDict:
        return
    className = specDict['complexType']['name']
    MODULES_QUEUE.add(className)
    print('Queued for writing: %s'%list(MODULES_QUEUE))
    baseTypeNode = specDict['complexType']['complexContent'].get('restriction', None) 
    if baseTypeNode is not None: 
        native, classBase = extractType(baseTypeNode['base'])
    else:
        baseTypeNode = specDict['complexType']['complexContent']['extension']
        native, classBase = extractType(baseTypeNode['base'])
    if not native:
        if not classBase in ALL_MODULES:
            processClassSpec(extractClassSpec(getClassDocUrl(HOST, classBase),  classBase), asText)
    typeClass = AgilityType(className, classBase if not native else None)
    sequence = baseTypeNode.get('sequence', None)
    if sequence is None or not sequence:
        elements = []
    else: 
        elements = sequence.get('element', None)
        if elements is None:
            print('Warning can not parse spec, skipping class [%s]'%className)
            return
        elements = elements if isinstance(elements, list) else [elements]
    
    attributes = baseTypeNode.get('attribute', [])
    attributes = attributes if isinstance(attributes, list) else [attributes]
    for attr in elements + attributes:
        if not isinstance(attr, dict):
            raise RuntimeError('attr : [%s] expected dict but is %s'(attr, type(attr)))
        nativeAttr, attrType = extractType(attr['type'])
        if not nativeAttr:
            if not attrType in ALL_MODULES and attrType != className and attrType not in MODULES_QUEUE:#break recursive loop for composites containing children of the same type
                processClassSpec(extractClassSpec(getClassDocUrl(HOST, attrType), attrType, asText))
        attr['native'] = nativeAttr
        attr['type'] = attrType
        typeClass.addAttribute(**attr)
    
    typeClass.write()
    
        
def extractType(typeText):
    agilityTypeQualifier = '{http://servicemesh.com/agility/api}'
    xmlTypeQualifier = '{http://www.w3.org/2001/XMLSchema}'
    native = False
    qualifier = ''
    if re.search(agilityTypeQualifier, typeText):
        qualifier = agilityTypeQualifier
    elif re.search(xmlTypeQualifier, typeText):
        qualifier = xmlTypeQualifier
        native = True
        
    return native, re.sub(qualifier, '', typeText)

class AgilityTypeAttribute(object):
    def __init__(self, **kwargs):
        nameSymbol = kwargs['name']
        if not isValidPythonSymbol(nameSymbol, False):
            validNameSymbol = validPythonSymbol(nameSymbol, False)
            print('WARNING: Python reserved symbol [%s] -> changed to [%s]'%(nameSymbol, validNameSymbol))
            kwargs['name'] = validNameSymbol
        
        kwargs['name'] = kwargs['name'].lower()#looks more consistent and would make the Ruby interpreter happy if the attribute name == a class name
        self.attrSpecs = kwargs         
        self.__dict__.update(kwargs)
        self.isOptional = '0' == getattr(self, 'minOccurs', '1')#if minOccurs is missing, then it's mandatory
        self.isContainer = '0' != getattr(self, 'maxOccurs', '0')#if missing, then not a container. if exists, should be > 0 => 'unbounded' might be the only value
        #default for containers = list()
        #default for optional = None
        #default for non-native (model object reference) = None
        #default for mandatory is TRICKY! '' for strings and None for everything else for now
        self.defaultValue = self._attrDefaultValueFactory()
        docLines = {}
        docLine = '@param %(name)s: %(name)s'
        docLine += ' minOccurs=%(minOccurs)s' if getattr(self, 'minOccurs', None) else ''
        docLine += ' maxOccurs=%(maxOccurs)s' if getattr(self, 'maxOccurs', None) else ''
        docLines['python'] = [docLine%self.__dict__, '@type %(name)s: %(type)s'%self.__dict__]
        
        
        self.doc = docLines
        
    def _attrDefaultValueFactory(self):
        EMPTY_STRING = "''"
        
        nativeTypeDefaultMap = {'python' : 
                                     {'string' : EMPTY_STRING,
                                  'boolean' : 'False', #consider auto boxing
                                  'int' : 'None',
                                  'integer' : 'None',
                                  'decimal' : 'None',
                                  'date' : 'None', 
                                  'dateTime' : 'None', 
                                  'hexBinary' : 'None',
                                  'base64Binary' : 'None',
                                  'long' : 'None',
                                  'double' : 'None',
                                  'float' : 'None',
                                  'container' : '[]',
                                  'NULL' : 'None'
                                  },
                             'ruby' :
                                     {'string' : EMPTY_STRING,
                                  'boolean' : 'false', #consider auto boxing
                                  'int' : 'nil',
                                  'integer' : 'nil',
                                  'decimal' : 'nil',
                                  'date' : 'nil', 
                                  'hexBinary' : 'nil',
                                  'base64Binary' : 'nil',
                                  'long' : 'nil',
                                  'double' : 'nil',
                                  'float' : 'nil',
                                  'container' : '[]',
                                  'NULL' : 'nil'
                              }
                                } 

        defaultValue = 'None'
        if self.isContainer:
            defaultValue = nativeTypeDefaultMap[LANG]['container']
        elif self.isOptional:
            defaultValue = nativeTypeDefaultMap[LANG]['NULL']
        elif self.native:
            try:
                return nativeTypeDefaultMap[LANG][self.type]
            except KeyError as ex:
                print(ex)
                raise RuntimeError('Unhandled XML native type: %s'%self.type)
        return defaultValue
    
class AgilityType(object):
    INDENT = ' '*4 if LANG == PYTHON else ' '*2
    CLASS_BASE_TEMPLATE = {}
    CLASS_BASE_TEMPLATE[PYTHON] = """%(imports)s

class %(Clazz)sBase(%(BaseClazz)s):
    '''
    classdocs
    '''
    def __init__(self%(comma)s%(kwargs)s):
        %(BaseClazz)s.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update(%(atrrSpecs)s)
        %(selfAttrs)s 
"""

    CLASS_BASE_TEMPLATE[RUBY] = """require 'base/%(BaseClazz)s'

class %(Clazz)sBase < %(BaseClazz)s
  %(attr_accessors)s
  def initialize(%(kwargs)s)
    super()
    @_attrSpecs.update(%(attrSpecs)s)
    %(selfAttrs)s
  end
end
"""

    CLASS_ACTION_TEMPLATE = {}
    CLASS_ACTION_TEMPLATE[PYTHON] = """%(imports)s

class %(Clazz)sActions(object):
    def __init__(self, *args, **kwargs):
        pass
"""

    CLASS_ACTION_TEMPLATE[RUBY] = """module %(Clazz)sActions
end
"""

    CLASS_TEMPLATE = {}
    CLASS_TEMPLATE[PYTHON] = """%(imports)s

class %(Clazz)s(%(Clazz)sBase, %(Clazz)sActions):
    '''
    classdocs
    '''
    def __init__(self%(comma)s%(kwargs)s):
        '''
        Constructor
        %(argdocs)s
        '''
        %(Clazz)sBase.__init__(self%(comma)s%(kwargsDelegation)s)
"""

    CLASS_TEMPLATE[RUBY] = """require 'base/%(Clazz)sBase'
require 'actions/%(Clazz)sActions'

class %(Clazz)s < %(Clazz)sBase
  include %(Clazz)sActions 
  def initialize(%(kwargs)s)
    super(%(kwargsDelegation)s)
  end
end
""" 
    def __init__(self, name, baseName=None):
        self.name = name
        self.baseName = baseName
        self.attrs = {}
    
    def addAttribute(self, **kwargs):
        self.attrs[kwargs['name']] = AgilityTypeAttribute(**kwargs)
        #Note: even in the case that attr name is invalid symbol and has to be changed, the original would still be used as a key to preserve the mapping e.g. Class._attrSpecs[ORIGINAL] = {'name' : MODIFIED}
    
    def write(self, dirname=''):
        dirname = dirname or rootDirName()
        
        basefilepath = os.path.join(dirname, 'base', (self.name if LANG == PYTHON else self.name + 'Base') + CODE_FILE_EXTENSION)
        actionsfilepath = os.path.join(dirname, 'actions', (self.name if LANG == PYTHON else self.name + 'Actions') + CODE_FILE_EXTENSION)
        classfilepath = os.path.join(dirname, self.name + CODE_FILE_EXTENSION)
        
        print('Writing [3] files: \n1.%s\n2.%s\n3.%s'%(basefilepath, actionsfilepath, classfilepath))
        basecode, actionscode, classcode = self.formatPython() if LANG == PYTHON else self.formatRuby()
        with open(basefilepath, 'w') as baseClassFile:
            baseClassFile.write(basecode)
        with open(actionsfilepath, 'w') as actionsClassFile:
            actionsClassFile.write(actionscode)
        with open(classfilepath, 'w') as actionsClassFile:
            actionsClassFile.write(classcode)
        ALL_MODULES.add(self.name)
        MODULES_QUEUE.remove(self.name)
        if LANG == PYTHON:
            with open(os.path.join(dirname, 'base', '__init__.py'), 'w') as packageInitFile:
                imports = '\n'.join(['from %(cls)s import %(cls)sBase'%{'cls' : cls} for cls in ALL_MODULES - ALL_ENUMS])
                packageInitFile.write(imports)
                packageInitFile.write('\n__all__ = %s'%list(['%sBase'%cls for cls in ALL_MODULES - ALL_ENUMS]))
            with open(os.path.join(dirname, 'actions', '__init__.py'), 'w') as packageInitFile:
                imports = '\n'.join(['from %(cls)s import %(cls)sActions'%{'cls' : cls} for cls in ALL_MODULES - ALL_ENUMS])
                packageInitFile.write(imports)
                packageInitFile.write('\n__all__ = %s'%list(['%sActions'%cls for cls in ALL_MODULES - ALL_ENUMS]))
            with open(os.path.join(dirname, '__init__.py'), 'w') as packageInitFile:
                imports = '\n'.join(['from %(cls)s import %(cls)s'%{'cls' : cls} for cls in ALL_MODULES])
                packageInitFile.write(imports)
                packageInitFile.write('\n__all__ = %s'%list(ALL_MODULES))
            print('agilitymodel.<base.|actions.|.>__init.__all__ = %s'%list(ALL_MODULES))
        
    def formatRuby(self):
        SUPER_BASE = 'AgilityModelBase'
        kwargs = ', '.join(['%s=%s'%(attr.name, attr.defaultValue) for attr in self.attrs.values()])
        kwargsDelegation = ', '.join(['%s=%s'%(attr.name, attr.name) for attr in self.attrs.values()])
        base_context = {
                   'Clazz' : self.name,
                   'BaseClazz' : self.baseName + 'Base' if self.baseName else SUPER_BASE,
                   'kwargs' : kwargs,
                   'selfAttrs' : ('\n%s'%(AgilityType.INDENT*2)).join(['@%s = %s'%(attr.name, attr.name) for attr in self.attrs.values()]),
                   'attrSpecs' : str(dict(zip([attrname for attrname in self.attrs], [attr.attrSpecs for attr in self.attrs.values()]))).replace('False', 'false').replace('True', 'true').replace(':', '=>'),
                   'attr_accessors' : ('\n%s'%(AgilityType.INDENT)).join(['attr_accessor :%s'%attr.name for attr in self.attrs.values()]),
                   }
        base_code =  AgilityType.CLASS_BASE_TEMPLATE[LANG]%base_context
        
        actions_context = {
                   'Clazz' : self.name
                   }
        actions_code = AgilityType.CLASS_ACTION_TEMPLATE[LANG]%actions_context
        
        class_context = {
                   'Clazz' : self.name,
                   'kwargs' : kwargs,
                   'kwargsDelegation' : kwargsDelegation
                   }
        class_code = AgilityType.CLASS_TEMPLATE[LANG]%class_context
        
        return base_code, actions_code, class_code
        
    def formatPython(self):
        SUPER_BASE = 'AgilityModelBase'
        base_imports = ['from %s import %s'%(self.baseName, self.baseName + 'Base')] if self.baseName and not self.baseName.startswith('{') else ['from core.agility.common.%(SUPER_BASE)s import %(SUPER_BASE)s'%{'SUPER_BASE' : SUPER_BASE}] 
        comma = ', ' if self.attrs else ''
        kwargs = ', '.join(['%s=%s'%(attr.name, attr.defaultValue) for attr in self.attrs.values()])
        kwargsDelegation = ', '.join(['%s=%s'%(attr.name, attr.name) for attr in self.attrs.values()])
        base_context = {
                   'imports' : '\n'.join(base_imports),
                   'Clazz' : self.name,
                   'BaseClazz' : self.baseName + 'Base' if self.baseName and not self.baseName.startswith('{') else SUPER_BASE,
                   'comma' : comma,
                   'kwargs' : kwargs,
                   'atrrSpecs' : '%s'%dict(zip([attrname for attrname in self.attrs], [attr.attrSpecs for attr in self.attrs.values()])),
                   'selfAttrs' : ('\n%s'%(AgilityType.INDENT*2)).join(['self.%s = %s'%(attr.name, attr.name) for attr in self.attrs.values()])
                   }
        base_code =  AgilityType.CLASS_BASE_TEMPLATE[LANG]%base_context
        
        actions_context = {
                   'imports' : '',
                   'Clazz' : self.name
                   }
        actions_context.update({'imports' : '', 'selfAttrs' : ''})
        actions_code = AgilityType.CLASS_ACTION_TEMPLATE[LANG]%actions_context
        
        class_imports = ['from %s.%s import %s'%('base', self.name, self.name + 'Base'), 'from %s.%s import %s'%('actions', self.name, self.name + 'Actions')]
        class_context = {
                   'imports' : '\n'.join(class_imports),
                   'Clazz' : self.name,
                   'comma' : comma,
                   'kwargs' : kwargs,
                   'argdocs' : ('\n%s'%(AgilityType.INDENT*2)).join([docline for docline in chain(*[attr.doc[PYTHON] for attr in self.attrs.values()])]),
                   'kwargsDelegation' : kwargsDelegation
                   }
        class_code = AgilityType.CLASS_TEMPLATE[LANG]%class_context
        
        return base_code, actions_code, class_code
    

def rootDirName():
    return os.path.dirname(agilitymodel.__file__) if LANG == PYTHON else os.path.join(os.path.dirname(agilitymodel.__file__), 'ruby') 

def parseXSDSpecs():
    pass
    
def parseHTMLSpecs():
    dirname = rootDirName()
    basedir = os.path.join(dirname, 'base')
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    actionsdir = os.path.join(dirname, 'actions')
    if not os.path.exists(actionsdir):
        os.makedirs(actionsdir)

    for classDocUrl in getAllClassesDocsUrls(host=HOST):
        specDict = extractClassSpec(classDocUrl, asText=False)
        processClassSpec(specDict)
    dirname = rootDirName()
    with open(os.path.join(dirname, 'Enums' + CODE_FILE_EXTENSION), 'w') as enumsModule:
        if LANG == PYTHON:
            enumsModule.write('\n__all__ = %s\n'%list(ALL_ENUMS))
            imports = '\n'.join(['from %(cls)s import %(cls)s'%{'cls' : cls} for cls in ALL_ENUMS])
            enumsModule.write(imports)
        elif LANG == RUBY:
            requires = '\n'.join(["require '%(cls)s'"%{'cls' : cls} for cls in ALL_ENUMS])
            enumsModule.write(requires)
            
    print('Rejected spec URLs: %s'%list(REJECTED_SPECS))
    print('Queue final status: %s'%list(MODULES_QUEUE))


def generateSchema():
    schemaContent = ""
    for classDocUrl in getAllClassesDocsUrls(host=HOST):
        classSpec = extractClassSpec(classDocUrl, asText=True) or ''
        SEP = '\n' if classSpec else ''
        schemaContent += (SEP + classSpec)

    print(schemaContent)
    
if __name__ == '__main__':
    schemaMode = configuration.get(section='main', option='schemaMode')  
    if schemaMode:
        generateSchema()
    else:
        parseHTMLSpecs()
