from ServiceMeshList import ServiceMeshListBase

class CustomContainerListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, customcontainer=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'customContainer': {'maxOccurs': 'unbounded', 'type': 'CustomContainer', 'name': 'customcontainer', 'minOccurs': '0', 'native': False}})
        self.customcontainer = customcontainer 
