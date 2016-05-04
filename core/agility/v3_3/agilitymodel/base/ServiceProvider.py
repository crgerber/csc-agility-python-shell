from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ServiceProviderBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, hostname=None, locations=[], properties=[], credentials=None, type=None, networks=[], cloud=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'hostname': {'type': 'string', 'name': 'hostname', 'minOccurs': '0', 'native': True}, 'locations': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'locations', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'credentials': {'type': 'Credential', 'name': 'credentials', 'minOccurs': '0', 'native': False}, 'type': {'type': 'Link', 'name': 'type', 'minOccurs': '0', 'native': False}, 'networks': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'networks', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.hostname = hostname
        self.locations = locations
        self.properties = properties
        self.credentials = credentials
        self.type = type
        self.networks = networks
        self.cloud = cloud 
