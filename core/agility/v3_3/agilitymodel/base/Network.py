from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class NetworkBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, serviceprovider=[], status=None, networkgateway=None, networkid=None, networkmask=None, dnsdomain=None, tenantid=None, subnets=[], addressrange=[], dnsservers=None, networkaddress=None, dsnsearch=[], routerexternal=None, shared=None, adminstateup=None, networkprovider=None, cloud=None, locations=[], ports=[]):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'networkGateway': {'native': True, 'name': 'networkgateway', 'minOccurs': '0', 'type': 'string'}, 'networkId': {'native': True, 'name': 'networkid', 'minOccurs': '0', 'type': 'string'}, 'networkMask': {'native': True, 'name': 'networkmask', 'minOccurs': '0', 'type': 'string'}, 'locations': {'maxOccurs': 'unbounded', 'native': False, 'name': 'locations', 'minOccurs': '0', 'type': 'Link'}, 'dsnSearch': {'maxOccurs': 'unbounded', 'native': True, 'name': 'dsnsearch', 'minOccurs': '0', 'type': 'string'}, 'dnsDomain': {'native': True, 'name': 'dnsdomain', 'minOccurs': '0', 'type': 'string'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'subnets': {'maxOccurs': 'unbounded', 'native': False, 'name': 'subnets', 'minOccurs': '0', 'type': 'Link'}, 'addressRange': {'maxOccurs': 'unbounded', 'native': False, 'name': 'addressrange', 'minOccurs': '0', 'type': 'Link'}, 'dnsServers': {'native': True, 'name': 'dnsservers', 'minOccurs': '0', 'type': 'string'}, 'serviceProvider': {'maxOccurs': 'unbounded', 'native': False, 'name': 'serviceprovider', 'minOccurs': '0', 'type': 'Link'}, 'tenantId': {'native': True, 'name': 'tenantid', 'minOccurs': '0', 'type': 'string'}, 'routerExternal': {'native': True, 'name': 'routerexternal', 'minOccurs': '0', 'type': 'boolean'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'adminStateUp': {'native': True, 'name': 'adminstateup', 'minOccurs': '0', 'type': 'boolean'}, 'networkAddress': {'native': True, 'name': 'networkaddress', 'minOccurs': '0', 'type': 'string'}, 'networkProvider': {'native': False, 'name': 'networkprovider', 'minOccurs': '0', 'type': 'Link'}, 'shared': {'native': True, 'name': 'shared', 'minOccurs': '0', 'type': 'boolean'}, 'ports': {'maxOccurs': 'unbounded', 'native': False, 'name': 'ports', 'minOccurs': '0', 'type': 'Link'}})
        self.serviceprovider = serviceprovider
        self.status = status
        self.networkgateway = networkgateway
        self.networkid = networkid
        self.networkmask = networkmask
        self.dnsdomain = dnsdomain
        self.tenantid = tenantid
        self.subnets = subnets
        self.addressrange = addressrange
        self.dnsservers = dnsservers
        self.networkaddress = networkaddress
        self.dsnsearch = dsnsearch
        self.routerexternal = routerexternal
        self.shared = shared
        self.adminstateup = adminstateup
        self.networkprovider = networkprovider
        self.cloud = cloud
        self.locations = locations
        self.ports = ports 
