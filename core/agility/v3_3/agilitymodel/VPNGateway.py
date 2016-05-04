from core.agility.v3_3.agilitymodel.base.VPNGateway import VPNGatewayBase
from core.agility.v3_3.agilitymodel.actions.VPNGateway import VPNGatewayActions

class VPNGateway(VPNGatewayBase, VPNGatewayActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, availabilityzone=None, type=None, vpngatewayid=None, attachment=[]):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param availabilityzone: availabilityzone minOccurs=0
        @type availabilityzone: string
        @param type: type minOccurs=0
        @type type: string
        @param vpngatewayid: vpngatewayid minOccurs=0
        @type vpngatewayid: string
        @param attachment: attachment minOccurs=0 maxOccurs=unbounded
        @type attachment: AttachmentType
        '''
        VPNGatewayBase.__init__(self, status=status, availabilityzone=availabilityzone, type=type, vpngatewayid=vpngatewayid, attachment=attachment)
