from core.agility.v3_3.agilitymodel.base.ServiceProviderType import ServiceProviderTypeBase

class NetworkServiceTypeBase(ServiceProviderTypeBase):
    '''
    classdocs
    '''
    def __init__(self, services=[], properties=[]):
        ServiceProviderTypeBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'services': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'services', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinition', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.services = services
        self.properties = properties 
