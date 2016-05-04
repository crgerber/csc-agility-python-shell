from SdnItem import SdnItemBase

class NetworkBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, networkid=None, subnets=[], adminstateup=None, networkaddress=None, dnsdomain=None, serviceprovider=[], addressrange=[], locations=[], dsnsearch=[], tenantid=None, status=None, networkprovider=None, networkgateway=None, shared=None, routerexternal=None, networkmask=None, dnsservers=None, cloud=None, ports=[]):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'networkId': {'type': 'string', 'name': 'networkid', 'minOccurs': '0', 'native': True}, 'subnets': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'subnets', 'minOccurs': '0', 'native': False}, 'addressRange': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'addressrange', 'minOccurs': '0', 'native': False}, 'networkAddress': {'type': 'string', 'name': 'networkaddress', 'minOccurs': '0', 'native': True}, 'dnsDomain': {'type': 'string', 'name': 'dnsdomain', 'minOccurs': '0', 'native': True}, 'serviceProvider': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'serviceprovider', 'minOccurs': '0', 'native': False}, 'adminStateUp': {'type': 'boolean', 'name': 'adminstateup', 'minOccurs': '0', 'native': True}, 'locations': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'locations', 'minOccurs': '0', 'native': False}, 'dsnSearch': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'dsnsearch', 'minOccurs': '0', 'native': True}, 'tenantId': {'type': 'string', 'name': 'tenantid', 'minOccurs': '0', 'native': True}, 'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'networkProvider': {'type': 'Link', 'name': 'networkprovider', 'minOccurs': '0', 'native': False}, 'networkGateway': {'type': 'string', 'name': 'networkgateway', 'minOccurs': '0', 'native': True}, 'networkMask': {'type': 'string', 'name': 'networkmask', 'minOccurs': '0', 'native': True}, 'routerExternal': {'type': 'boolean', 'name': 'routerexternal', 'minOccurs': '0', 'native': True}, 'shared': {'type': 'boolean', 'name': 'shared', 'minOccurs': '0', 'native': True}, 'dnsServers': {'type': 'string', 'name': 'dnsservers', 'minOccurs': '0', 'native': True}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'ports': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'ports', 'minOccurs': '0', 'native': False}})
        self.networkid = networkid
        self.subnets = subnets
        self.adminstateup = adminstateup
        self.networkaddress = networkaddress
        self.dnsdomain = dnsdomain
        self.serviceprovider = serviceprovider
        self.addressrange = addressrange
        self.locations = locations
        self.dsnsearch = dsnsearch
        self.tenantid = tenantid
        self.status = status
        self.networkprovider = networkprovider
        self.networkgateway = networkgateway
        self.shared = shared
        self.routerexternal = routerexternal
        self.networkmask = networkmask
        self.dnsservers = dnsservers
        self.cloud = cloud
        self.ports = ports 
