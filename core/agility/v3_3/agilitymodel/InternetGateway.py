from base.InternetGateway import InternetGatewayBase
from actions.InternetGateway import InternetGatewayActions

class InternetGateway(InternetGatewayBase, InternetGatewayActions):
    '''
    classdocs
    '''
    def __init__(self, internetgatewayid=None, attachment=[]):
        '''
        Constructor
        @param internetgatewayid: internetgatewayid minOccurs=0
        @type internetgatewayid: string
        @param attachment: attachment minOccurs=0 maxOccurs=unbounded
        @type attachment: AttachmentType
        '''
        InternetGatewayBase.__init__(self, internetgatewayid=internetgatewayid, attachment=attachment)
