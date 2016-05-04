from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class NetworkProviderTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, version=None, type=None, properties=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'version': {'type': 'string', 'name': 'version', 'minOccurs': '0', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.version = version
        self.type = type
        self.properties = properties 
