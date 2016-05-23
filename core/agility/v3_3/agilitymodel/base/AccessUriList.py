from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class AccessUriListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, accessuri=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'AccessUri': {'name': 'accessuri', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AccessUri'}})
        self.accessuri = accessuri 
