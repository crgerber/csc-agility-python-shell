from core.agility.v3_3.agilitymodel.base.ServiceProviderType import ServiceProviderTypeBase

class NetworkServiceTypeBase(ServiceProviderTypeBase):
    '''
    classdocs
    '''
    def __init__(self, services=[], properties=[]):
        ServiceProviderTypeBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'services': {'maxOccurs': 'unbounded', 'native': True, 'name': 'services', 'minOccurs': '0', 'type': 'string'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'PropertyDefinition'}})
        self.services = services
        self.properties = properties 
