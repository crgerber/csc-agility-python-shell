from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class ArtifactTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, platformServiceType=None, properties=list()):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'platformServiceType': {'type': 'Link', 'name': 'platformServiceType', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.platformServiceType = platformServiceType
        self.properties = properties 
