from Item import ItemBase

class NetworkServiceBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, hostname=None, networks=list(), credentials=None, type=None, properties=list(), cloud=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'hostname': {'type': 'string', 'name': 'hostname', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'credentials': {'type': 'Credential', 'name': 'credentials', 'minOccurs': '0', 'native': False}, 'type': {'type': 'Link', 'name': 'type', 'minOccurs': '0', 'native': False}, 'networks': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'networks', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.hostname = hostname
        self.networks = networks
        self.credentials = credentials
        self.type = type
        self.properties = properties
        self.cloud = cloud 
