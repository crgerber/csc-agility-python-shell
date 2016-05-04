from base.VPNConnection import VPNConnectionBase
from actions.VPNConnection import VPNConnectionActions

class VPNConnection(VPNConnectionBase, VPNConnectionActions):
    '''
    classdocs
    '''
    def __init__(self, vpnconnectionid=None, status=None, customergatewayconfiguration=None, customergateway=None, vpngateway=None, type=None):
        '''
        Constructor
        @param vpnconnectionid: vpnconnectionid minOccurs=0
        @type vpnconnectionid: string
        @param status: status minOccurs=0
        @type status: string
        @param customergatewayconfiguration: customergatewayconfiguration minOccurs=0
        @type customergatewayconfiguration: string
        @param customergateway: customergateway minOccurs=0
        @type customergateway: CustomerGateway
        @param vpngateway: vpngateway minOccurs=0
        @type vpngateway: VPNGateway
        @param type: type minOccurs=0
        @type type: string
        '''
        VPNConnectionBase.__init__(self, vpnconnectionid=vpnconnectionid, status=status, customergatewayconfiguration=customergatewayconfiguration, customergateway=customergateway, vpngateway=vpngateway, type=type)
