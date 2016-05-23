from core.agility.v3_3.agilitymodel.base.ServiceProviderType import ServiceProviderTypeBase

class NetworkServiceTypeBase(ServiceProviderTypeBase):
    '''
    classdocs
    '''
    def __init__(self, services=[], properties=[]):
        ServiceProviderTypeBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'services': {'name': 'services', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PropertyDefinition'}})
        self.services = services
        self.properties = properties 
