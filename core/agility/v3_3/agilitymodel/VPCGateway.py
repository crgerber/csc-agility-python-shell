from base.VPCGateway import VPCGatewayBase
from actions.VPCGateway import VPCGatewayActions

class VPCGateway(VPCGatewayBase, VPCGatewayActions):
    '''
    classdocs
    '''
    def __init__(self, vpngateway=None, properties=[], vpnconnection=None, vpc=None, customergateway=None):
        '''
        Constructor
        @param vpngateway: vpngateway minOccurs=0
        @type vpngateway: VPNGateway
        @param properties: properties minOccurs=0 maxOccurs=unbounded
        @type properties: Property
        @param vpnconnection: vpnconnection minOccurs=0
        @type vpnconnection: VPNConnection
        @param vpc: vpc minOccurs=0
        @type vpc: VPC
        @param customergateway: customergateway minOccurs=0
        @type customergateway: CustomerGateway
        '''
        VPCGatewayBase.__init__(self, vpngateway=vpngateway, properties=properties, vpnconnection=vpnconnection, vpc=vpc, customergateway=customergateway)
