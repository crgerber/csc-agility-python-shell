from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ServiceProviderBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, credentials=None, networks=[], properties=[], type=None, cloud=None, hostname=None, locations=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credentials': {'native': False, 'name': 'credentials', 'minOccurs': '0', 'type': 'Credential'}, 'locations': {'maxOccurs': 'unbounded', 'native': False, 'name': 'locations', 'minOccurs': '0', 'type': 'Link'}, 'networks': {'maxOccurs': 'unbounded', 'native': False, 'name': 'networks', 'minOccurs': '0', 'type': 'Link'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'AssetProperty'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'hostname': {'native': True, 'name': 'hostname', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': False, 'name': 'type', 'minOccurs': '0', 'type': 'Link'}})
        self.credentials = credentials
        self.networks = networks
        self.properties = properties
        self.type = type
        self.cloud = cloud
        self.hostname = hostname
        self.locations = locations 
