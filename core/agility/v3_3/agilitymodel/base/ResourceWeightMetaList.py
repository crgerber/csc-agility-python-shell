from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class ResourceWeightMetaListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, resourceweightmeta=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resourceWeightMeta': {'name': 'resourceweightmeta', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ResourceWeightMeta'}})
        self.resourceweightmeta = resourceweightmeta 
