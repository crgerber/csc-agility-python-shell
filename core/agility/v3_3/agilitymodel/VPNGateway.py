from core.agility.v3_3.agilitymodel.base.VPNGateway import VPNGatewayBase
from core.agility.v3_3.agilitymodel.actions.VPNGateway import VPNGatewayActions

class VPNGateway(VPNGatewayBase, VPNGatewayActions):
    '''
    classdocs
    '''
    def __init__(self, attachment=[], vpngatewayid=None, availabilityzone=None, status=None, type=None):
        '''
        Constructor
        @param attachment: attachment minOccurs=0 maxOccurs=unbounded
        @type attachment: AttachmentType
        @param vpngatewayid: vpngatewayid minOccurs=0
        @type vpngatewayid: string
        @param availabilityzone: availabilityzone minOccurs=0
        @type availabilityzone: string
        @param status: status minOccurs=0
        @type status: string
        @param type: type minOccurs=0
        @type type: string
        '''
        VPNGatewayBase.__init__(self, attachment=attachment, vpngatewayid=vpngatewayid, availabilityzone=availabilityzone, status=status, type=type)
