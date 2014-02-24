from agilityshell import agility
import core.restclient.gen.methods as client
from core.restclient.responseparser.common import AbstractProxy
from core.restclient.agility.assettype import ASSET_TYPES
from functools import partial
from core.proxy.serviceproxy import ParseDecorator

DISPLAY_NAME_ASSET_TYPE_MAP = agility.tools.scripting.idmap(ASSET_TYPES, 'displayName')

class Asset(AbstractProxy):
    _BASE_ATTRIBUTES = ['name', 'description']
    def __init__(self, typeName, name='', description=''):
        attrs = dict(zip(Asset._BASE_ATTRIBUTES, [name, description]))
        AbstractProxy.__init__(self, attrs=attrs, typeName=typeName)
        self._autoattrs += ['_top', '_serviceendpoint']
        self._top = True
        _serviceendpointName = DISPLAY_NAME_ASSET_TYPE_MAP[typeName]['serviceendpoint']
        self._serviceendpoint = getattr(client, _serviceendpointName, None)
    
#    def __getattr__(self, name):
#        result = None
#        if name in object.__getattribute__(self, '_autoattrs'):
#            result = object.__getattribute__(self, name)
#        elif name in object.__getattribute__(self, '_attrs'):
#            result = self.__getitem__(name)
#        else:
#            method = getattr(self._serviceendpoint, name, None)
#            if not method:
#                raise AttributeError(name)
#            result = ParseDecorator(self.typeName)(method)
#            result.context = method.context
#        return result
             
    def __setattr__(self, name, value):
        #mark nested composites as so
        if isinstance(value, Asset):
            value._top = False
        AbstractProxy.__setattr__(self, name, value)
        return self #allow method chaining
            
    def __str__(self):
        return agility.tools.crud.createTemplate(self.typeName, **self._attrs)
    
    def _load(self, proxy):
        self._attrs.update(proxy._attrs)

    
class Script(Asset):
    def __init__(self, name='', description=''):
        Asset.__init__(self, 'Script', name, description)
    
class AssetFactory(object):
    def __init__(self, agility):
        self._agility = agility
        
        
    def __dir__(self):
        return [asset['displayName'] for asset in ASSET_TYPES]
    
    def __getattr__(self, name):
        if name not in DISPLAY_NAME_ASSET_TYPE_MAP:
            raise AttributeError, name
        asset = partial(Asset, name)
        
        return asset
        
        
