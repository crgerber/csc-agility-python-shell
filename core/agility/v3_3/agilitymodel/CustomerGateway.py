from core.agility.v3_3.agilitymodel.base.CustomerGateway import CustomerGatewayBase
from core.agility.v3_3.agilitymodel.actions.CustomerGateway import CustomerGatewayActions

class CustomerGateway(CustomerGatewayBase, CustomerGatewayActions):
    '''
    classdocs
    '''
    def __init__(self, bgpasn=None, ipaddress=None, status=None, type=None, customergatewayid=None):
        '''
        Constructor
        @param bgpasn: bgpasn minOccurs=0
        @type bgpasn: int
        @param ipaddress: ipaddress minOccurs=0
        @type ipaddress: string
        @param status: status minOccurs=0
        @type status: string
        @param type: type minOccurs=0
        @type type: string
        @param customergatewayid: customergatewayid minOccurs=0
        @type customergatewayid: string
        '''
        CustomerGatewayBase.__init__(self, bgpasn=bgpasn, ipaddress=ipaddress, status=status, type=type, customergatewayid=customergatewayid)
