from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PlatformServiceTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, runtimeproperties=[], servicetypes=[], properties=[], type='', artifacttypes=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'runtimeProperties': {'name': 'runtimeproperties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'artifactTypes': {'name': 'artifacttypes', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ArtifactType'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'type': {'name': 'type', 'native': True, 'type': 'string'}, 'serviceTypes': {'name': 'servicetypes', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ServiceBindingType'}})
        self.runtimeproperties = runtimeproperties
        self.servicetypes = servicetypes
        self.properties = properties
        self.type = type
        self.artifacttypes = artifacttypes 
