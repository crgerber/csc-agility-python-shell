from Item import ItemBase

class VPCBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, mainroutetable=None, vpcid=None, instancetenancy=None, customergateway=[], subnet=[], dhcpoptions=None, defaultvpc=None, virtualprivategateway=None, securitygroup=[], properties=[], instance=[], vpnconnection=[], internetgateway=None, otherroutetable=[], cidrblock=None, networks=[], cloud=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'mainRouteTable': {'type': 'RouteTable', 'name': 'mainroutetable', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'vpcId': {'type': 'string', 'name': 'vpcid', 'minOccurs': '0', 'native': True}, 'instanceTenancy': {'type': 'string', 'name': 'instancetenancy', 'minOccurs': '0', 'native': True}, 'subnet': {'maxOccurs': 'unbounded', 'type': 'VPCSubnet', 'name': 'subnet', 'minOccurs': '0', 'native': False}, 'dhcpOptions': {'type': 'DhcpOptions', 'name': 'dhcpoptions', 'minOccurs': '0', 'native': False}, 'networks': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'networks', 'minOccurs': '0', 'native': False}, 'customerGateway': {'maxOccurs': 'unbounded', 'type': 'CustomerGateway', 'name': 'customergateway', 'minOccurs': '0', 'native': False}, 'securityGroup': {'maxOccurs': 'unbounded', 'type': 'SecurityGroup', 'name': 'securitygroup', 'minOccurs': '0', 'native': False}, 'virtualPrivateGateway': {'type': 'VPNGateway', 'name': 'virtualprivategateway', 'minOccurs': '0', 'native': False}, 'instance': {'maxOccurs': 'unbounded', 'type': 'Instance', 'name': 'instance', 'minOccurs': '0', 'native': False}, 'vpnConnection': {'maxOccurs': 'unbounded', 'type': 'VPNConnection', 'name': 'vpnconnection', 'minOccurs': '0', 'native': False}, 'internetGateway': {'type': 'InternetGateway', 'name': 'internetgateway', 'minOccurs': '0', 'native': False}, 'otherRouteTable': {'maxOccurs': 'unbounded', 'type': 'RouteTable', 'name': 'otherroutetable', 'minOccurs': '0', 'native': False}, 'cidrBlock': {'type': 'string', 'name': 'cidrblock', 'minOccurs': '0', 'native': True}, 'defaultVpc': {'type': 'boolean', 'name': 'defaultvpc', 'minOccurs': '0', 'native': True}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.status = status
        self.mainroutetable = mainroutetable
        self.vpcid = vpcid
        self.instancetenancy = instancetenancy
        self.customergateway = customergateway
        self.subnet = subnet
        self.dhcpoptions = dhcpoptions
        self.defaultvpc = defaultvpc
        self.virtualprivategateway = virtualprivategateway
        self.securitygroup = securitygroup
        self.properties = properties
        self.instance = instance
        self.vpnconnection = vpnconnection
        self.internetgateway = internetgateway
        self.otherroutetable = otherroutetable
        self.cidrblock = cidrblock
        self.networks = networks
        self.cloud = cloud 
