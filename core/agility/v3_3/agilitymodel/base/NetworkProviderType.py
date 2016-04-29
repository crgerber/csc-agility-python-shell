from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class NetworkProviderTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, version=None, properties=[], type=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'version': {'native': True, 'name': 'version', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': True, 'name': 'type', 'minOccurs': '0', 'type': 'string'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}})
        self.version = version
        self.properties = properties
        self.type = type 
