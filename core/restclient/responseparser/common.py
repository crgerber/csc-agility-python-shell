'''
Created on Oct 19, 2012

@author: dawood
'''
import os
import logger
import time
from collections import defaultdict
import re

import unicodedata


TAG_HIERARCHIES = [('Linklist', 'link'), ('Assetlist', 'Asset')]
TAG_HIERARCHIES_MAP = {'Linklist' : 'link', 'Assetlist' : 'Asset'}

COMPONENT_NAME = 'agilityclient'
logger = logger.getLogger(COMPONENT_NAME)


def decode(data):
    if not isinstance(data, unicode):
        return str(data)
    else:
        return unicodedata.normalize('NFKD', data).encode('ascii','ignore')

class AbstractProxy(object):
    
    def __init__(self, attrs=None, typeName=''):
        '''        
        example input param = {'Script': {'creator': [{'name': ['admin'], 'href': ['https://localhost:8443/agility/api/current/user/1'], 'rel': ['up'], 'position': ['0'], 'type': ['application/com.servicemesh.agility.api.User+xml'], 'id': ['1']}], 'runAsAdmin': ['false'], 'id': ['104'], 'assetType': [{'name': ['script'], 'href': ['https://localhost:8443/agility/api/current/assettype/2'], 'rel': ['up'], 'position': ['0'], 'type': ['application/com.servicemesh.agility.api.AssetType+xml'], 'id': ['2']}], 'assetPath': ['/Root/SHADOW/Project101'], 'uuid': ['ba93106a-da1f-4c26-8a46-940556842bb7'], 'top': ['false'], 'version': ['-1'], 'removable': ['true'], 'type': ['Guest'], 'description': ['Test Script for Test Bench Development'], 'parent': [{'name': ['Project101'], 'href': ['https://localhost:8443/agility/api/current/project/29'], 'rel': ['up'], 'position': ['0'], 'type': ['application/com.servicemesh.agility.api.Project+xml'], 'id': ['29']}], 'enableExtensions': ['false'], 'lockType': ['0'], 'publisher': [{'name': ['admin'], 'href': ['https://localhost:8443/agility/api/current/user/1'], 'rel': ['up'], 'position': ['0'], 'type': ['application/com.servicemesh.agility.api.User+xml'], 'id': ['1']}], 'name': ['TEST SCRIPT 102'], 'created': ['2012-10-15T00:46:52-04:00'], 'lastModified': ['2012-10-15T00:46:52-04:00'], 'lifecycleVersion': ['-1'], 'timeout': ['3600'], 'operatingSystem': ['Unknown'], 'latest': ['false']}}
        '''
        object.__setattr__(self, '_autoattrs', ['_autoattrs', 'typeName', '_attrs', '_initialized', '_topLevel'])
        object.__setattr__(self, 'typeName', typeName if typeName else AbstractProxy._extractTypeName(attrs))
        object.__setattr__(self, '_attrs',  {} if attrs is None else attrs)
        object.__setattr__(self, '_initialized', False)
        object.__setattr__(self, '_topLevel', False)
        
                
    def __repr__(self):
        '''
        xml structure doesn't treat nested asset entries, or nested lists of assets in the same way as the top level asset
        '''
        if self._topLevel:
            return repr({self.typeName : self._attrs})
        else:
            return repr(self._attrs)
    
    def __str__(self):
        return str(self._attrs)
    
#    def __len__(self):
#        return len(self._attrs)
    
    def __dir__(self):
        return self.__dict__.keys() + self._attrs.keys()
    
    def __getattr__(self, name):
        if name in object.__getattribute__(self, '_autoattrs'):
            return object.__getattribute__(self, name)
        if name not in object.__getattribute__(self, '_attrs'):
            raise AttributeError, name
        return self.__getitem__(name)
    
    def __setattr__(self, name, value):
        if name in self._autoattrs:
            return object.__setattr__(self, name, value)
        
        self.__setitem__(name, value)
        
    def __delattr__(self, name):
        if name in self._autoattrs:
            return object.__delattr__(self, name)
        
        self.__delitem__(name)
    
    def _newSubObject(self, attrs):
        raise NotImplementedError('sub object factory method is not defined for type: %s'%self.__class__.__name__)
           
    def __getitem__(self, key):
        return self._attrs[key]
    
    def get(self, key, default=None, mustbe=None, wrapper=None):
        '''
        similar behavior to dict.get
        
        @param mustbe: class, type, or tuple of classes and types, will be used for isintance check, a ValueError is raised if type doesn't match expectations
        @param wrapper: a callable, that accepts a single argument. wrapper would get a chance to reformat (re-cast) the value
        a typical use case is when API's inconsistently report an attribute as a single instance OR list
        
        example: asList = lambda attr: attr if isinstance(attr, (tuple, list)) else [attr]
        since otherwise, client code might be iterating over the wrong sequence, e.g. object attribute names instead of list of objects 
        '''
        attr = self._attrs.get(key, default)
        if mustbe is not None and attr is not None:
            if not isinstance(attr, mustbe):
                raise ValueError('attribute of type [%s], expected type(s): [%s]'%(type(attr), mustbe))
        return wrapper(attr) if wrapper else attr
    
    def __setitem__(self, key, value):
        self._attrs[key] = value
    
    def __delitem__(self, key):
        del self._attrs[key]
    
    def __iter__(self):
        return iter(self._attrs)
    
    def __contains__(self, item):
        return item in self._attrs
    
    def __hash__(self):
        return hash(self._attrs)
    
    def __eq__(self, other):
        if not other or not isinstance(other, AbstractProxy):
            return False
        return self._attrs == other._attrs
    
    def __ne__(self, other):
        return not self.__eq__(other)
    
    def _getXmlText(self):
        raise NotImplementedError('%s does not implement _getXmlText'%self.__class__.__name__)
    
    def _asMap(self):
        return self._attrs

    def save(self, persistDir='snapshot', persistFile=''):
        timestamp = time.strftime('%Y%m%d%H%M%S')
        persistFile = persistFile or '%s_%s_%s.xml'%(self.id, self.typeName, timestamp)
        persistXML(self._getXmlText(), persistDir, persistFile)
        
    @classmethod
    def _extractTypeName(cls, attrs):
        typeName = ''
        if attrs is None:
            return typeName
        typeUrl = attrs.get('type', None)
        typeUrl = decode(typeUrl[0] if isinstance(typeUrl, (list, tuple)) else typeUrl) 
        TYPE_NAME = 'TYPE_NAME'
        if typeUrl:
            match = re.match('application/com\.servicemesh\.agility\.api\.(?P<TYPE_NAME>.*)\+xml', typeUrl)
            if match:
                typeName = match.groupdict()[TYPE_NAME]
        return typeName

def persistXML(xmlText, persistDir='', persistFile=''):
    if not all([persistDir, persistFile]):
        logger.info('No persisting params specified')
        return True
    if not os.path.exists(persistDir):
        os.makedirs(persistDir)
    xmlFilePath = os.path.join(persistDir, persistFile)
    with open(xmlFilePath, 'w') as xmlFile:
        xmlFile.write(xmlText)
        logger.info('Persistent xml file: %s created successfully', xmlFilePath)
    return True
        
class persist(object):
    doc = 'Function is decorated to persist xml result if arguments "persistDir" and "persistFile" are supplied'
    def __init__(self, f):
        self.f = f
        self.__name__ = f.__name__
        self.__doc__ = '%s\n%s'%(persist.doc, f.__doc__)

    def __call__(self, *args, **kwargs):
        if kwargs:
            persistDir = kwargs.pop('persistDir', '')
            persistFile = kwargs.pop('persistFile', '')
            xmlText = args[0]
            if all([persistDir, persistFile]):
                persistXML(xmlText, persistDir, persistFile)
        return self.f(*args, **kwargs)
        
