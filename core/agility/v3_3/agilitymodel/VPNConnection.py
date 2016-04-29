from core.agility.v3_3.agilitymodel.base.VPNConnection import VPNConnectionBase
from core.agility.v3_3.agilitymodel.actions.VPNConnection import VPNConnectionActions

class VPNConnection(VPNConnectionBase, VPNConnectionActions):
    '''
    classdocs
    '''
    def __init__(self, customergateway=None, customergatewayconfiguration=None, vpnconnectionid=None, status=None, vpngateway=None, type=None):
        '''
        Constructor
        @param customergateway: customergateway minOccurs=0
        @type customergateway: CustomerGateway
        @param customergatewayconfiguration: customergatewayconfiguration minOccurs=0
        @type customergatewayconfiguration: string
        @param vpnconnectionid: vpnconnectionid minOccurs=0
        @type vpnconnectionid: string
        @param status: status minOccurs=0
        @type status: string
        @param vpngateway: vpngateway minOccurs=0
        @type vpngateway: VPNGateway
        @param type: type minOccurs=0
        @type type: string
        '''
        VPNConnectionBase.__init__(self, customergateway=customergateway, customergatewayconfiguration=customergatewayconfiguration, vpnconnectionid=vpnconnectionid, status=status, vpngateway=vpngateway, type=type)
