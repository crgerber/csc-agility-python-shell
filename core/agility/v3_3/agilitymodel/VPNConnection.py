from core.agility.v3_3.agilitymodel.base.VPNConnection import VPNConnectionBase
from core.agility.v3_3.agilitymodel.actions.VPNConnection import VPNConnectionActions

class VPNConnection(VPNConnectionBase, VPNConnectionActions):
    '''
    classdocs
    '''
    def __init__(self, vpnconnectionid=None, customergatewayconfiguration=None, customergateway=None, vpngateway=None, type=None, status=None):
        '''
        Constructor
        @param vpnconnectionid: vpnconnectionid minOccurs=0
        @type vpnconnectionid: string
        @param customergatewayconfiguration: customergatewayconfiguration minOccurs=0
        @type customergatewayconfiguration: string
        @param customergateway: customergateway minOccurs=0
        @type customergateway: CustomerGateway
        @param vpngateway: vpngateway minOccurs=0
        @type vpngateway: VPNGateway
        @param type: type minOccurs=0
        @type type: string
        @param status: status minOccurs=0
        @type status: string
        '''
        VPNConnectionBase.__init__(self, vpnconnectionid=vpnconnectionid, customergatewayconfiguration=customergatewayconfiguration, customergateway=customergateway, vpngateway=vpngateway, type=type, status=status)
