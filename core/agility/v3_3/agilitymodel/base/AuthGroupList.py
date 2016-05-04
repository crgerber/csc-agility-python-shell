from ServiceMeshList import ServiceMeshListBase

class AuthGroupListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, mappings=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'mappings': {'maxOccurs': 'unbounded', 'type': 'AuthGroup', 'name': 'mappings', 'minOccurs': '0', 'native': False}})
        self.mappings = mappings 
