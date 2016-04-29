from core.agility.v3_3.agilitymodel.base.InternetGateway import InternetGatewayBase
from core.agility.v3_3.agilitymodel.actions.InternetGateway import InternetGatewayActions

class InternetGateway(InternetGatewayBase, InternetGatewayActions):
    '''
    classdocs
    '''
    def __init__(self, attachment=[], internetgatewayid=None):
        '''
        Constructor
        @param attachment: attachment minOccurs=0 maxOccurs=unbounded
        @type attachment: AttachmentType
        @param internetgatewayid: internetgatewayid minOccurs=0
        @type internetgatewayid: string
        '''
        InternetGatewayBase.__init__(self, attachment=attachment, internetgatewayid=internetgatewayid)
