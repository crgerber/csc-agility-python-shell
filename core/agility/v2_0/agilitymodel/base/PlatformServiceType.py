from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class PlatformServiceTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, artifactTypes=list(), runtimeProperties=list(), serviceTypes=list(), type='', properties=list()):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'serviceTypes': {'maxOccurs': 'unbounded', 'type': 'ServiceBindingType', 'name': 'serviceTypes', 'minOccurs': '0', 'native': False}, 'runtimeProperties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'runtimeProperties', 'minOccurs': '0', 'native': False}, 'artifactTypes': {'maxOccurs': 'unbounded', 'type': 'ArtifactType', 'name': 'artifactTypes', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'native': True}})
        self.artifactTypes = artifactTypes
        self.runtimeProperties = runtimeProperties
        self.serviceTypes = serviceTypes
        self.type = type
        self.properties = properties 
