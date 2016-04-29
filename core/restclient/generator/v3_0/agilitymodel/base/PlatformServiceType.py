from .Asset import AssetBase

class PlatformServiceTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, artifacttypes=[], runtimeproperties=[], servicetypes=[], type='', properties=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'serviceTypes': {'maxOccurs': 'unbounded', 'type': 'ServiceBindingType', 'name': 'servicetypes', 'minOccurs': '0', 'native': False}, 'runtimeProperties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'runtimeproperties', 'minOccurs': '0', 'native': False}, 'artifactTypes': {'maxOccurs': 'unbounded', 'type': 'ArtifactType', 'name': 'artifacttypes', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'native': True}})
        self.artifacttypes = artifacttypes
        self.runtimeproperties = runtimeproperties
        self.servicetypes = servicetypes
        self.type = type
        self.properties = properties 
