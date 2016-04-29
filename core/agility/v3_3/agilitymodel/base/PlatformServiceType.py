from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PlatformServiceTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, servicetypes=[], properties=[], artifacttypes=[], runtimeproperties=[], type=''):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'serviceTypes': {'maxOccurs': 'unbounded', 'native': False, 'name': 'servicetypes', 'minOccurs': '0', 'type': 'ServiceBindingType'}, 'type': {'native': True, 'name': 'type', 'type': 'string'}, 'runtimeProperties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'runtimeproperties', 'minOccurs': '0', 'type': 'Property'}, 'artifactTypes': {'maxOccurs': 'unbounded', 'native': False, 'name': 'artifacttypes', 'minOccurs': '0', 'type': 'ArtifactType'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}})
        self.servicetypes = servicetypes
        self.properties = properties
        self.artifacttypes = artifacttypes
        self.runtimeproperties = runtimeproperties
        self.type = type 
