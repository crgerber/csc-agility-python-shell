from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class NetworkBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, networkid=None, serviceprovider=[], tenantid=None, networkprovider=None, adminstateup=None, routerexternal=None, dnsservers=None, dnsdomain=None, addressrange=[], locations=[], status=None, cloud=None, networkmask=None, networkaddress=None, subnets=[], ports=[], dsnsearch=[], shared=None, networkgateway=None):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'networkId': {'name': 'networkid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'serviceProvider': {'name': 'serviceprovider', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'tenantId': {'name': 'tenantid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'adminStateUp': {'name': 'adminstateup', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'dsnSearch': {'name': 'dsnsearch', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'dnsServers': {'name': 'dnsservers', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'dnsDomain': {'name': 'dnsdomain', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'addressRange': {'name': 'addressrange', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'locations': {'name': 'locations', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'networkMask': {'name': 'networkmask', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'networkProvider': {'name': 'networkprovider', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'shared': {'name': 'shared', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'subnets': {'name': 'subnets', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'ports': {'name': 'ports', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'routerExternal': {'name': 'routerexternal', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'networkAddress': {'name': 'networkaddress', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'networkGateway': {'name': 'networkgateway', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.networkid = networkid
        self.serviceprovider = serviceprovider
        self.tenantid = tenantid
        self.networkprovider = networkprovider
        self.adminstateup = adminstateup
        self.routerexternal = routerexternal
        self.dnsservers = dnsservers
        self.dnsdomain = dnsdomain
        self.addressrange = addressrange
        self.locations = locations
        self.status = status
        self.cloud = cloud
        self.networkmask = networkmask
        self.networkaddress = networkaddress
        self.subnets = subnets
        self.ports = ports
        self.dsnsearch = dsnsearch
        self.shared = shared
        self.networkgateway = networkgateway 
