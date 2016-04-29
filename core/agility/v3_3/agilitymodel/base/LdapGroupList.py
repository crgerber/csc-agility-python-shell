from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class LdapGroupListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, mappings=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'mappings': {'maxOccurs': 'unbounded', 'native': False, 'name': 'mappings', 'minOccurs': '0', 'type': 'LdapGroup'}})
        self.mappings = mappings 
