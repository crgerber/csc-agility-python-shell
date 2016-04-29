from core.agility.v3_3.agilitymodel.base.VPC import VPCBase
from core.agility.v3_3.agilitymodel.actions.VPC import VPCActions

class VPC(VPCBase, VPCActions):
    '''
    classdocs
    '''
    def __init__(self, vpnconnection=[], defaultvpc=None, networks=[], properties=[], mainroutetable=None, internetgateway=None, status=None, subnet=[], customergateway=[], vpcid=None, securitygroup=[], otherroutetable=[], instancetenancy=None, instance=[], cloud=None, cidrblock=None, dhcpoptions=None, virtualprivategateway=None):
        '''
        Constructor
        @param vpnconnection: vpnconnection minOccurs=0 maxOccurs=unbounded
        @type vpnconnection: VPNConnection
        @param defaultvpc: defaultvpc minOccurs=0
        @type defaultvpc: boolean
        @param networks: networks minOccurs=0 maxOccurs=unbounded
        @type networks: Link
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param mainroutetable: mainroutetable minOccurs=0
        @type mainroutetable: RouteTable
        @param internetgateway: internetgateway minOccurs=0
        @type internetgateway: InternetGateway
        @param status: status minOccurs=0
        @type status: string
        @param subnet: subnet minOccurs=0 maxOccurs=unbounded
        @type subnet: VPCSubnet
        @param customergateway: customergateway minOccurs=0 maxOccurs=unbounded
        @type customergateway: CustomerGateway
        @param vpcid: vpcid minOccurs=0
        @type vpcid: string
        @param securitygroup: securitygroup minOccurs=0 maxOccurs=unbounded
        @type securitygroup: SecurityGroup
        @param otherroutetable: otherroutetable minOccurs=0 maxOccurs=unbounded
        @type otherroutetable: RouteTable
        @param instancetenancy: instancetenancy minOccurs=0
        @type instancetenancy: string
        @param instance: instance minOccurs=0 maxOccurs=unbounded
        @type instance: Instance
        @param cloud: cloud minOccurs=0
        @type cloud: Link
        @param cidrblock: cidrblock minOccurs=0
        @type cidrblock: string
        @param dhcpoptions: dhcpoptions minOccurs=0
        @type dhcpoptions: DhcpOptions
        @param virtualprivategateway: virtualprivategateway minOccurs=0
        @type virtualprivategateway: VPNGateway
        '''
        VPCBase.__init__(self, vpnconnection=vpnconnection, defaultvpc=defaultvpc, networks=networks, properties=properties, mainroutetable=mainroutetable, internetgateway=internetgateway, status=status, subnet=subnet, customergateway=customergateway, vpcid=vpcid, securitygroup=securitygroup, otherroutetable=otherroutetable, instancetenancy=instancetenancy, instance=instance, cloud=cloud, cidrblock=cidrblock, dhcpoptions=dhcpoptions, virtualprivategateway=virtualprivategateway)
