from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VPCBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, vpnconnection=[], defaultvpc=None, networks=[], properties=[], mainroutetable=None, internetgateway=None, status=None, subnet=[], customergateway=[], vpcid=None, securitygroup=[], otherroutetable=[], instancetenancy=None, instance=[], cloud=None, cidrblock=None, dhcpoptions=None, virtualprivategateway=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'dhcpOptions': {'native': False, 'name': 'dhcpoptions', 'minOccurs': '0', 'type': 'DhcpOptions'}, 'vpnConnection': {'maxOccurs': 'unbounded', 'native': False, 'name': 'vpnconnection', 'minOccurs': '0', 'type': 'VPNConnection'}, 'customerGateway': {'maxOccurs': 'unbounded', 'native': False, 'name': 'customergateway', 'minOccurs': '0', 'type': 'CustomerGateway'}, 'instanceTenancy': {'native': True, 'name': 'instancetenancy', 'minOccurs': '0', 'type': 'string'}, 'securityGroup': {'maxOccurs': 'unbounded', 'native': False, 'name': 'securitygroup', 'minOccurs': '0', 'type': 'SecurityGroup'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'mainRouteTable': {'native': False, 'name': 'mainroutetable', 'minOccurs': '0', 'type': 'RouteTable'}, 'internetGateway': {'native': False, 'name': 'internetgateway', 'minOccurs': '0', 'type': 'InternetGateway'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'virtualPrivateGateway': {'native': False, 'name': 'virtualprivategateway', 'minOccurs': '0', 'type': 'VPNGateway'}, 'instance': {'maxOccurs': 'unbounded', 'native': False, 'name': 'instance', 'minOccurs': '0', 'type': 'Instance'}, 'vpcId': {'native': True, 'name': 'vpcid', 'minOccurs': '0', 'type': 'string'}, 'defaultVpc': {'native': True, 'name': 'defaultvpc', 'minOccurs': '0', 'type': 'boolean'}, 'otherRouteTable': {'maxOccurs': 'unbounded', 'native': False, 'name': 'otherroutetable', 'minOccurs': '0', 'type': 'RouteTable'}, 'networks': {'maxOccurs': 'unbounded', 'native': False, 'name': 'networks', 'minOccurs': '0', 'type': 'Link'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'cidrBlock': {'native': True, 'name': 'cidrblock', 'minOccurs': '0', 'type': 'string'}, 'subnet': {'maxOccurs': 'unbounded', 'native': False, 'name': 'subnet', 'minOccurs': '0', 'type': 'VPCSubnet'}})
        self.vpnconnection = vpnconnection
        self.defaultvpc = defaultvpc
        self.networks = networks
        self.properties = properties
        self.mainroutetable = mainroutetable
        self.internetgateway = internetgateway
        self.status = status
        self.subnet = subnet
        self.customergateway = customergateway
        self.vpcid = vpcid
        self.securitygroup = securitygroup
        self.otherroutetable = otherroutetable
        self.instancetenancy = instancetenancy
        self.instance = instance
        self.cloud = cloud
        self.cidrblock = cidrblock
        self.dhcpoptions = dhcpoptions
        self.virtualprivategateway = virtualprivategateway 
