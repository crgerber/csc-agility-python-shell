from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class CustomContainerListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, customcontainer=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'customContainer': {'name': 'customcontainer', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'CustomContainer'}})
        self.customcontainer = customcontainer 
