from ServiceMeshList import ServiceMeshListBase

class AccessUriListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, accessuri=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'AccessUri': {'maxOccurs': 'unbounded', 'type': 'AccessUri', 'name': 'accessuri', 'minOccurs': '0', 'native': False}})
        self.accessuri = accessuri 
