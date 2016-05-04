from base.VPC import VPCBase
from actions.VPC import VPCActions

class VPC(VPCBase, VPCActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, mainroutetable=None, vpcid=None, instancetenancy=None, customergateway=[], subnet=[], dhcpoptions=None, defaultvpc=None, virtualprivategateway=None, securitygroup=[], properties=[], instance=[], vpnconnection=[], internetgateway=None, otherroutetable=[], cidrblock=None, networks=[], cloud=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param mainroutetable: mainroutetable minOccurs=0
        @type mainroutetable: RouteTable
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param instancetenancy: instancetenancy minOccurs=0
        @type instancetenancy: string
        @param customergateway: customergateway minOccurs=0 maxOccurs=unbounded
        @type customergateway: CustomerGateway
        @param subnet: subnet minOccurs=0 maxOccurs=unbounded
        @type subnet: VPCSubnet
        @param dhcpoptions: dhcpoptions minOccurs=0
        @type dhcpoptions: DhcpOptions
        @param defaultvpc: defaultvpc minOccurs=0
        @type defaultvpc: boolean
        @param virtualprivategateway: virtualprivategateway minOccurs=0
        @type virtualprivategateway: VPNGateway
        @param securitygroup: securitygroup minOccurs=0 maxOccurs=unbounded
        @type securitygroup: SecurityGroup
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param instance: instance minOccurs=0 maxOccurs=unbounded
        @type instance: Instance
        @param vpnconnection: vpnconnection minOccurs=0 maxOccurs=unbounded
        @type vpnconnection: VPNConnection
        @param internetgateway: internetgateway minOccurs=0
        @type internetgateway: InternetGateway
        @param otherroutetable: otherroutetable minOccurs=0 maxOccurs=unbounded
        @type otherroutetable: RouteTable
        @param cidrblock: cidrblock minOccurs=0
        @type cidrblock: string
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        '''
        VPCBase.__init__(self, status=status, mainroutetable=mainroutetable, vpcid=vpcid, instancetenancy=instancetenancy, customergateway=customergateway, subnet=subnet, dhcpoptions=dhcpoptions, defaultvpc=defaultvpc, virtualprivategateway=virtualprivategateway, securitygroup=securitygroup, properties=properties, instance=instance, vpnconnection=vpnconnection, internetgateway=internetgateway, otherroutetable=otherroutetable, cidrblock=cidrblock, networks=networks, cloud=cloud)
