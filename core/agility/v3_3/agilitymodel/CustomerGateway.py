from base.CustomerGateway import CustomerGatewayBase
from actions.CustomerGateway import CustomerGatewayActions

class CustomerGateway(CustomerGatewayBase, CustomerGatewayActions):
    '''
    classdocs
    '''
    def __init__(self, customergatewayid=None, status=None, type=None, ipaddress=None, bgpasn=None):
        '''
        Constructor
        @param customergatewayid: customergatewayid minOccurs=0
        @type customergatewayid: string
        @param status: status minOccurs=0
        @type status: string
        @param type: type minOccurs=0
        @type type: string
        @param ipaddress: ipaddress minOccurs=0
        @type ipaddress: string
        @param bgpasn: bgpasn minOccurs=0
        @type bgpasn: int
        '''
        CustomerGatewayBase.__init__(self, customergatewayid=customergatewayid, status=status, type=type, ipaddress=ipaddress, bgpasn=bgpasn)
