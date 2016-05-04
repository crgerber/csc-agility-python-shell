from ServiceMeshList import ServiceMeshListBase

class ResourceWeightMetaListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, resourceweightmeta=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resourceWeightMeta': {'maxOccurs': 'unbounded', 'type': 'ResourceWeightMeta', 'name': 'resourceweightmeta', 'minOccurs': '0', 'native': False}})
        self.resourceweightmeta = resourceweightmeta 
