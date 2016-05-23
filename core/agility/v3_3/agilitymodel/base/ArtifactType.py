from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ArtifactTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, platformservicetype=None, properties=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'platformServiceType': {'name': 'platformservicetype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}})
        self.platformservicetype = platformservicetype
        self.properties = properties 
