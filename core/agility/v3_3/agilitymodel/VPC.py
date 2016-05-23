from core.agility.v3_3.agilitymodel.base.VPC import VPCBase
from core.agility.v3_3.agilitymodel.actions.VPC import VPCActions

class VPC(VPCBase, VPCActions):
    '''
    classdocs
    '''
    def __init__(self, properties=[], instancetenancy=None, instance=[], cidrblock=None, dhcpoptions=None, defaultvpc=None, vpcid=None, vpnconnection=[], cloud=None, virtualprivategateway=None, networks=[], internetgateway=None, mainroutetable=None, customergateway=[], subnet=[], securitygroup=[], otherroutetable=[], status=None):
        '''
        Constructor
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param instancetenancy: instancetenancy minOccurs=0
        @type instancetenancy: string
        @param instance: instance minOccurs=0 maxOccurs=unbounded
        @type instance: Instance
        @param cidrblock: cidrblock minOccurs=0
        @type cidrblock: string
        @param dhcpoptions: dhcpoptions minOccurs=0
        @type dhcpoptions: DhcpOptions
        @param defaultvpc: defaultvpc minOccurs=0
        @type defaultvpc: boolean
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param vpnconnection: vpnconnection minOccurs=0 maxOccurs=unbounded
        @type vpnconnection: VPNConnection
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param virtualprivategateway: virtualprivategateway minOccurs=0
        @type virtualprivategateway: VPNGateway
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param internetgateway: internetgateway minOccurs=0
        @type internetgateway: InternetGateway
        @param mainroutetable: mainroutetable minOccurs=0
        @type mainroutetable: RouteTable
        @param customergateway: customergateway minOccurs=0 maxOccurs=unbounded
        @type customergateway: CustomerGateway
        @param subnet: subnet minOccurs=0 maxOccurs=unbounded
        @type subnet: VPCSubnet
        @param securitygroup: securitygroup minOccurs=0 maxOccurs=unbounded
        @type securitygroup: SecurityGroup
        @param otherroutetable: otherroutetable minOccurs=0 maxOccurs=unbounded
        @type otherroutetable: RouteTable
        @param status: status minOccurs=0
        @type status: string
        '''
        VPCBase.__init__(self, properties=properties, instancetenancy=instancetenancy, instance=instance, cidrblock=cidrblock, dhcpoptions=dhcpoptions, defaultvpc=defaultvpc, vpcid=vpcid, vpnconnection=vpnconnection, cloud=cloud, virtualprivategateway=virtualprivategateway, networks=networks, internetgateway=internetgateway, mainroutetable=mainroutetable, customergateway=customergateway, subnet=subnet, securitygroup=securitygroup, otherroutetable=otherroutetable, status=status)
