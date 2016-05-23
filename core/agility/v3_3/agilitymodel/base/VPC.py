from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VPCBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, properties=[], instancetenancy=None, instance=[], cidrblock=None, dhcpoptions=None, defaultvpc=None, vpcid=None, vpnconnection=[], cloud=None, virtualprivategateway=None, networks=[], internetgateway=None, mainroutetable=None, customergateway=[], subnet=[], securitygroup=[], otherroutetable=[], status=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'instanceTenancy': {'name': 'instancetenancy', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'cidrBlock': {'name': 'cidrblock', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'dhcpOptions': {'name': 'dhcpoptions', 'minOccurs': '0', 'native': False, 'type': 'DhcpOptions'}, 'defaultVpc': {'name': 'defaultvpc', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'vpcId': {'name': 'vpcid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'vpnConnection': {'name': 'vpnconnection', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'VPNConnection'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'virtualPrivateGateway': {'name': 'virtualprivategateway', 'minOccurs': '0', 'native': False, 'type': 'VPNGateway'}, 'otherRouteTable': {'name': 'otherroutetable', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'RouteTable'}, 'internetGateway': {'name': 'internetgateway', 'minOccurs': '0', 'native': False, 'type': 'InternetGateway'}, 'mainRouteTable': {'name': 'mainroutetable', 'minOccurs': '0', 'native': False, 'type': 'RouteTable'}, 'customerGateway': {'name': 'customergateway', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'CustomerGateway'}, 'subnet': {'name': 'subnet', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'VPCSubnet'}, 'securityGroup': {'name': 'securitygroup', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'SecurityGroup'}, 'networks': {'name': 'networks', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'instance': {'name': 'instance', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Instance'}})
        self.properties = properties
        self.instancetenancy = instancetenancy
        self.instance = instance
        self.cidrblock = cidrblock
        self.dhcpoptions = dhcpoptions
        self.defaultvpc = defaultvpc
        self.vpcid = vpcid
        self.vpnconnection = vpnconnection
        self.cloud = cloud
        self.virtualprivategateway = virtualprivategateway
        self.networks = networks
        self.internetgateway = internetgateway
        self.mainroutetable = mainroutetable
        self.customergateway = customergateway
        self.subnet = subnet
        self.securitygroup = securitygroup
        self.otherroutetable = otherroutetable
        self.status = status 
