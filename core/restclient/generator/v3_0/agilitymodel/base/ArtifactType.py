from .Asset import AssetBase

class ArtifactTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, platformservicetype=None, properties=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'platformServiceType': {'type': 'Link', 'name': 'platformservicetype', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.platformservicetype = platformservicetype
        self.properties = properties 
