from core.agility.v3_3.agilitymodel.base.VPCGateway import VPCGatewayBase
from core.agility.v3_3.agilitymodel.actions.VPCGateway import VPCGatewayActions

class VPCGateway(VPCGatewayBase, VPCGatewayActions):
    '''
    classdocs
    '''
    def __init__(self, vpnconnection=None, vpc=None, customergateway=None, vpngateway=None, properties=[]):
        '''
        Constructor
        @param vpnconnection: vpnconnection minOccurs=0
        @type vpnconnection: VPNConnection
        @param vpc: vpc minOccurs=0
        @type vpc: VPC
        @param customergateway: customergateway minOccurs=0
        @type customergateway: CustomerGateway
        @param vpngateway: vpngateway minOccurs=0
        @type vpngateway: VPNGateway
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        '''
        VPCGatewayBase.__init__(self, vpnconnection=vpnconnection, vpc=vpc, customergateway=customergateway, vpngateway=vpngateway, properties=properties)
