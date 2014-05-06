from Item import ItemBase

class NetworkBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, networkid=None, networkaddress=None, dnsdomain=None, addressrange=[], locations=[], dsnsearch=[], properties=[], networkgateway=None, networkmask=None, dnsservers=None, cloud=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'networkId': {'type': 'string', 'name': 'networkid', 'minOccurs': '0', 'native': True}, 'networkAddress': {'type': 'string', 'name': 'networkaddress', 'minOccurs': '0', 'native': True}, 'dnsDomain': {'type': 'string', 'name': 'dnsdomain', 'minOccurs': '0', 'native': True}, 'addressRange': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'addressrange', 'minOccurs': '0', 'native': False}, 'locations': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'locations', 'minOccurs': '0', 'native': False}, 'dsnSearch': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'dsnsearch', 'minOccurs': '0', 'native': True}, 'dnsServers': {'type': 'string', 'name': 'dnsservers', 'minOccurs': '0', 'native': True}, 'networkGateway': {'type': 'string', 'name': 'networkgateway', 'minOccurs': '0', 'native': True}, 'networkMask': {'type': 'string', 'name': 'networkmask', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.networkid = networkid
        self.networkaddress = networkaddress
        self.dnsdomain = dnsdomain
        self.addressrange = addressrange
        self.locations = locations
        self.dsnsearch = dsnsearch
        self.properties = properties
        self.networkgateway = networkgateway
        self.networkmask = networkmask
        self.dnsservers = dnsservers
        self.cloud = cloud 
