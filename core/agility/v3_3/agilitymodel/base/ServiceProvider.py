from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ServiceProviderBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, credentials=None, type=None, cloud=None, properties=[], networks=[], hostname=None, locations=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credentials': {'name': 'credentials', 'minOccurs': '0', 'native': False, 'type': 'Credential'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'locations': {'name': 'locations', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'hostname': {'name': 'hostname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'networks': {'name': 'networks', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.credentials = credentials
        self.type = type
        self.cloud = cloud
        self.properties = properties
        self.networks = networks
        self.hostname = hostname
        self.locations = locations 
