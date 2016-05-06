from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class AuthenticationListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, authentications=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'authentications': {'maxOccurs': 'unbounded', 'type': 'Authentication', 'name': 'authentications', 'minOccurs': '0', 'native': False}})
        self.authentications = authentications 
