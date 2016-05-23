from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class NetworkProviderTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, properties=[], type=None, version=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'version': {'name': 'version', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.properties = properties
        self.type = type
        self.version = version 
