from core.agility.v3_3.agilitymodel.base.VPCGateway import VPCGatewayBase
from core.agility.v3_3.agilitymodel.actions.VPCGateway import VPCGatewayActions

class VPCGateway(VPCGatewayBase, VPCGatewayActions):
    '''
    classdocs
    '''
    def __init__(self, customergateway=None, properties=[], vpnconnection=None, vpc=None, vpngateway=None):
        '''
        Constructor
        @param customergateway: customergateway minOccurs=0
        @type customergateway: CustomerGateway
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param vpnconnection: vpnconnection minOccurs=0
        @type vpnconnection: VPNConnection
        @param vpc: vpc minOccurs=0
        @type vpc: VPC
        @param vpngateway: vpngateway minOccurs=0
        @type vpngateway: VPNGateway
        '''
        VPCGatewayBase.__init__(self, customergateway=customergateway, properties=properties, vpnconnection=vpnconnection, vpc=vpc, vpngateway=vpngateway)
