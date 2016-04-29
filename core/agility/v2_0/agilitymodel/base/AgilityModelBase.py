'''
Created on Apr 19, 2013

@author: dawood
'''
from core.base.enum import Enum
from core.restclient.responseparser.LxmlTools import d2xml, assetToXMLTemplate
import re
import time
from core.restclient.responseparser.common import persistXML, AbstractProxy
from logger import logger

class AgilityModelBase(object):
    def __init__(self, *args, **kwrags):
        self.typeName = self.__class__.__name__
        self._topLevel = True
        #importing agility at the top of the module will not have access to the agility object yet
        from agilityshell import agility
        self._apiversion_compatibility = agility.cfg.configuration.get('apiversion', 'compatibility')  #@todo pass configuration in a more consistent way through out the library
    
    def _loadAttrs(self, attrs, classFactory, topLevel=True, wrapComposites=True):
        assert isinstance(attrs, dict)
        self._topLevel = topLevel
        self.typeName = self._extractTypeName(attrs) or self.typeName
        for attrName, attrVal in list(attrs.items()):
            #handle control tags, e.g. xsi, nsmap, etc ...
            if attrName.startswith('__') and attrName.endswith('__'):
                setattr(self, attrName, attrVal)
                continue
            
            attrSpec = self._attrSpecs.get(attrName, {})
            if not attrSpec:#No specs for attr
                if not isinstance(attrVal, dict):
                    attrSpec = {'type' : 'string',
                                'native' : True,
                                'name' : attrName}
                else:#dict
                    if self._apiversion_compatibility:
                        logger.warn('Skipping unexpected composite attribute [%s] : [%s]'%(attrName, attrVal))
                        continue
                    else:
                        raise RuntimeError('Unexpected composite attribute [%s] : [%s]'%(attrName, attrVal))
            if attrSpec['native']:
                setattr(self, attrSpec['name'], attrVal)
            else:
                clazz = classFactory(attrSpec['type'])
                #here, we might load the xsd:type xml attribute as the concrete type of the returned XML
                #Verify that the concrete type isinstance(spectype)
                #use a class of the concrete subtype to load the data to avoid data loss, as in the case of the NetworkInterface extending Resrouce
                if issubclass(clazz.__class__, Enum):
                    obj = attrVal#simple enum string value
                elif isinstance(attrVal, list):
                    #assert attrSpec['maxOccurs'] optionally
                    obj = [self._getSubTypeClass(clazz, subDct, classFactory)()._loadAttrs(subDct, classFactory, topLevel=False, wrapComposites=wrapComposites) for subDct in attrVal]
                else:
                    obj = self._getSubTypeClass(clazz, attrVal, classFactory)()._loadAttrs(attrVal, classFactory, topLevel=False, wrapComposites=wrapComposites)
                    #handle composite types, as a result of search query parameters to expand attributes of child Links
                    strType = obj.__class__.__name__.split('.')[-1]
                    childAttrName = {'Assetlist' : 'Asset',
                        'Linklist' : 'link',
                        'Tasklist' : 'Task'
                        }
                    
                    #NOTE:Below we can't use isinstance since importing those class will result in a module circular reference since AgilityModelBase is the super class of all other classes
                    if strType in ('Assetlist', 'Linklist', 'Tasklist'):
                        childAttr = getattr(obj, childAttrName[strType])
                        compositeName = getattr(obj, 'name', attrSpec['name'])
                        obj = childAttr if isinstance(childAttr, (list, tuple)) else [childAttr]
                        setattr(self, compositeName, obj)
                        continue #we don't want to fall through to the default attr setting logic with the name from attrSpec only, we'd end up with an attribute called AssetList for instance
                    elif wrapComposites and attrSpec.get('maxOccurs', None) == 'unbounded':
                        obj = [obj]
                        
                setattr(self, attrSpec['name'], obj)#note that attrName straight from XML might not be a valid Python symbol, attrSpec['name'] is the fixed version of that name
        return self
    
    def _getSubTypeClass(self, baseClass, attrDct, classFactory, typeFieldName='__xsi_type__'):
        subTypeClass = baseClass
        subTypeClassName = attrDct.get(typeFieldName, None)
        if not subTypeClassName: return subTypeClass #no inheritance type information in attribute dict, use base type from XSD
        subTypeClassName = subTypeClassName.split(':')[-1]#handle "ns1:className" format of the type attribute
        subTypeClass = classFactory(subTypeClassName)
        assert any([issubclass(subTypeClass, base) for base in baseClass.mro()])
        return subTypeClass
         
        
    
    def _extractTypeName(self, attrs=None):
        attrs = attrs or self
        typeName = ''

        typeUrl = attrs.get('type', None)
        typeUrl = typeUrl[0] if isinstance(typeUrl, (list, tuple)) else typeUrl if isinstance(typeUrl, str) else None
        TYPE_NAME = 'TYPE_NAME'
        if typeUrl:
            match = re.match('application/com\.servicemesh\.agility\.api\.(?P<TYPE_NAME>.*)\+xml', typeUrl)
            if match:
                typeName = match.groupdict()[TYPE_NAME]
        return typeName
    
    def _getXmlText(self):
        return d2xml(self._asMap(topLevel=True))
    
    def createXMLTemplate(self, deleteFields=None, replaceFields=None, asTopLevel=True, returnXMLOnly=True):
        '''
        Creates an XML document including all not None attributes of the asset at hand
        
        @param deleteFields: list of field names to be deleted, fully qualified names can be used, e.f. resources.<id>.network.href
        @param replaceFields: dict of field name, new value pairs
        @param asTopLevel: Treat the asset at hand as a top level asset while formating the XML document. Default: True
        @param returnXMLOnly: return only the XML string, if False, a a tuple containing: template XML string, template dictionary is returned
        @return: XML string if returnXMLOnly==True else a tuple containing: template XML string, template dictionary
        '''
        originalTopLeve = self._topLevel
        self._topLevel = asTopLevel
        xml, dct = assetToXMLTemplate(self, deleteFields, replaceFields)
        self._topLevel = originalTopLeve
        if returnXMLOnly:
            return xml
        else:
            return xml, dct
    
    def _asMap(self, topLevel=False, execludeEmptyFields=True, includeControlTags=True):
        asMap = lambda e: e._asMap() if isinstance(e, AgilityModelBase) else e
        topLevel = self._topLevel or topLevel
        reprMap = {k: v for k, v in list(vars(self).items()) if k.startswith('__') and k.endswith('__')}
        for k, v in list(self._attrSpecs.items()):
            attr = getattr(self, k, None)
            if execludeEmptyFields and not attr:#None, empty string, list, dict, etc ...
                continue
            elif isinstance(attr, list):
                reprMap[k] = [asMap(e) for e in attr]
            else:
                reprMap[k] = asMap(attr)
        if topLevel:
            return {self.typeName : reprMap}
        else:
            return reprMap
    
    def __dir__(self):
        return list(self._attrSpecs.keys()) + ['typeName']
    
    def __getitem__(self, key):
        return self._asMap()[key]
    
    def get(self, key, default=None, mustbe=None, wrapper=None):
        '''
        similar behavior to dict.get
        
        @param mustbe: class, type, or tuple of classes and types, will be used for isintance check, a ValueError is raised if type doesn't match expectations
        @param wrapper: a callable, that accepts a single argument. wrapper would get a chance to reformat (re-cast) the value
        a typical use case is when API's inconsistently report an attribute as a single instance OR list
        
        example: asList = lambda attr: attr if isinstance(attr, (tuple, list)) else [attr]
        since otherwise, client code might be iterating over the wrong sequence, e.g. object attribute names instead of list of objects 
        '''
        attr = self._asMap()[self.typeName].get(key, default)
        if mustbe is not None and attr is not None:
            if not isinstance(attr, mustbe):
                raise ValueError('attribute of type [%s], expected type(s): [%s]'%(type(attr), mustbe))
        return wrapper(attr) if wrapper else attr
    
    def __setitem__(self, key, value):
        self.key = value
    
    def __delitem__(self, key):
        delattr(self, key)
    
    def __iter__(self):
        return iter(self._asMap())
    
    def __contains__(self, item):
        return hasattr(object, item)
    
    def __hash__(self):
        return hash(self._asMap())
    
    def __eq__(self, other):
        if not other or not isinstance(other, (AgilityModelBase, AbstractProxy)):
            return False
        return self._asMap() == other._asMap()
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def save(self, persistDir='snapshot', persistFile=''):
        timestamp = time.strftime('%Y%m%d%H%M%S')
        persistFile = persistFile or '%s_%s_%s.xml'%(self.id, self.typeName, timestamp)
        persistXML(self._getXmlText(), persistDir, persistFile)
    
    def __repr__(self):
        return repr(self._asMap())
    
    __str__ = __repr__
