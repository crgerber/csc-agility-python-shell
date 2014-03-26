from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class NetworkBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, networkId=None, networkAddress=None, dnsDomain=None, addressRange=list(), locations=list(), dsnSearch=list(), properties=list(), networkGateway=None, networkMask=None, dnsServers=None, cloud=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'networkId': {'type': 'string', 'name': 'networkId', 'minOccurs': '0', 'native': True}, 'networkAddress': {'type': 'string', 'name': 'networkAddress', 'minOccurs': '0', 'native': True}, 'dnsDomain': {'type': 'string', 'name': 'dnsDomain', 'minOccurs': '0', 'native': True}, 'addressRange': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'addressRange', 'minOccurs': '0', 'native': False}, 'locations': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'locations', 'minOccurs': '0', 'native': False}, 'dsnSearch': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'dsnSearch', 'minOccurs': '0', 'native': True}, 'dnsServers': {'type': 'string', 'name': 'dnsServers', 'minOccurs': '0', 'native': True}, 'networkGateway': {'type': 'string', 'name': 'networkGateway', 'minOccurs': '0', 'native': True}, 'networkMask': {'type': 'string', 'name': 'networkMask', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.networkId = networkId
        self.networkAddress = networkAddress
        self.dnsDomain = dnsDomain
        self.addressRange = addressRange
        self.locations = locations
        self.dsnSearch = dsnSearch
        self.properties = properties
        self.networkGateway = networkGateway
        self.networkMask = networkMask
        self.dnsServers = dnsServers
        self.cloud = cloud 
