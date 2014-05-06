'''
Created on Dec 4, 2012

@author: dawood
'''
from core.restclient.responseparser.common import AbstractProxy
from core.base.enum import Enum
from core.restclient.responseparser.ParserBeautifulSoup import AssetEntryBeautifulSoup,\
    AssetAttributeBeautifulSoup
from core.restclient.responseparser.ParserLxml import AssetEntryLxml,\
    AssetAttributeLxml
__all__ = ['container', 'proxy']

from core.agility.common.servicelookup import lookup
from agilityshell import agility as a, agility
from logger import logger
import re
#some shorthands
idmap = a.tools.scripting.idmap
namemap = a.tools.scripting.namemap

validSymbol = a.tools.scripting.validSymbol

DEFAULT_TREE = {'container' : {
                               'container' : {}, 'customContainer' : {}, 'package' : {}, 'containerRight' : {}, 'policy' : {}, 'script' : {}, 'domain' : {}, 'project' : {}, 'stack' : {}
                               }
                }
TYPE = Enum(**{'ASSET_LIST' : 'AssetList',
               'ASSET_MAP' : 'AssetMap',
               'ASSET' : 'Asset',
               'ASSET_SUMMARY' : 'AssetSummary'
               })

containerTypes = ['Container', 'Project', 'Topology', 'Template', 'Stack', 'Package', 'Script', 'Instances', 'ContainerRight', 'Policy']

hasattrs = lambda obj, attrlist: all([getattr(obj, attr, None) for attr in attrlist])
allhaveattrs = lambda sequence, attrlist: all([hasattrs(item, attrlist) for item in sequence])


def deeptype(obj):
    idandtype = ['id', 'type']
    type_ = type(obj)
    if isinstance(obj, (list, tuple)):
        if allhaveattrs(obj, idandtype):
            type_ = TYPE.ASSET_LIST
    elif isinstance(obj, dict):
        if allhaveattrs(obj.values(), idandtype):
            type_ = TYPE.ASSET_MAP
    elif isinstance(obj, (AssetEntryBeautifulSoup, AssetEntryLxml)):
        type_ = TYPE.ASSET
#        if not getattr(obj, '_initialized', False):
#            type_ = TYPE.ASSET_SUMMARY
            
    elif isinstance(obj, (AssetAttributeBeautifulSoup, AssetAttributeLxml)):
        if hasattrs(obj, idandtype):
            type_ = TYPE.ASSET_SUMMARY
    return type_
    
        
    
def cleanidmap(iterable, key='id'):
    mapfunc = idmap if key=='id' else namemap
    id_map = {}
    if not iterable:
        return id_map
    if isinstance(iterable, (dict, AbstractProxy)):
        iterable = [iterable]
    [id_map.update([(validSymbol(id, key), obj)]) for id, obj in mapfunc(iterable).items()]
    return id_map
    
class AssetContainer(AbstractProxy):
    def __init__(self, iterable, typeName=None, useid=True, autoload=True, usehref=True, recursive=True):
        AbstractProxy.__init__(self, attrs=cleanidmap(iterable, 'id' if useid else 'name'), typeName=typeName)
        self._autoattrs += ['autoload', 'usehref', 'recursive', 'useid']
        self.autoload = autoload
        self.usehref = usehref
        self.recursive = recursive
        self.useid = useid
    
    def append(self, item):
        key = validSymbol(item.id, 'id') if self.useid else validSymbol(item.name, 'name')
        self._attrs[key] = item
        
    
    def _getTypeName(self, obj):
        typeName = 'Unknown'
        typeUrl = obj.get('type', None)
        TYPE_NAME = 'TYPE_NAME'
        if typeUrl:
            match = re.match('application/com\.servicemesh\.agility\.api\.(?P<TYPE_NAME>.*)\+xml', typeUrl)
            typeName = match.groupdict()[TYPE_NAME]
            if typeName and not self.typeName:
                self.typeName = typeName
        return typeName
    
    def __getattr__(self, name):
        item = AbstractProxy.__getattr__(self, name)
        result = item
        if not self.autoload:
            return result
        if not item._initialized:
            typeName = self._getTypeName(item)
            if typeName is None:
                return result
            href = getattr(item, 'href', None)
            if not self.usehref or href is None:
                serviceEndPoint = getattr(agility, typeName[0].lower() + typeName[1:])
                getserviceName = lookup(typeName, action=lookup.ACTION.GET)
                getservice = getattr(serviceEndPoint, getserviceName, None)
                if getservice is None:
                    logger.warning('No such service [%s] for asset [%s]', getserviceName, typeName)
                    return result
                result = getservice(item.id)
            else:
                logger.info('loading proxy using url %s', href)
                result = agility.tools.xml.parse(agility.cfg.conn.request(href).read(), assetType=typeName)
                if self.recursive:
                    result = proxy(result, useid=self.useid)
        result._initialized = True
        self._attrs[name] = result
        return result
    
#expose the constructor as a factory method
container = AssetContainer

def proxy(asset, typeName=None, useid=True, autoload=True, usehref=True, recursive=True):
    pop = False
    assetList = list(asset)
    if not isinstance(asset, (list, tuple)):
        pop = True#remember to pop the item from the list before return
        assetList = [asset]
    else:
        #copy the list
        assetList = list(asset)
    for assetEntry in assetList:
        for attrName in assetEntry:
            if attrName.capitalize() in containerTypes:
                logger.debug('Wrapping [%s] in a dynamic loader')
                attr = getattr(assetEntry, attrName)
                type_ = deeptype(attr)
                if type_ == TYPE.ASSET_SUMMARY:
                    setattr(assetEntry, attrName, container([attr], typeName, useid, autoload, usehref, recursive))
                elif type_ == TYPE.ASSET_LIST:
                    setattr(assetEntry, attrName, container(attr, typeName, useid, autoload, usehref, recursive))
    return assetList.pop() if pop else assetList