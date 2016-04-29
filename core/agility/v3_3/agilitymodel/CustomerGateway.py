from core.agility.v3_3.agilitymodel.base.CustomerGateway import CustomerGatewayBase
from core.agility.v3_3.agilitymodel.actions.CustomerGateway import CustomerGatewayActions

class CustomerGateway(CustomerGatewayBase, CustomerGatewayActions):
    '''
    classdocs
    '''
    def __init__(self, ipaddress=None, customergatewayid=None, bgpasn=None, status=None, type=None):
        '''
        Constructor
        @param ipaddress: ipaddress minOccurs=0
        @type ipaddress: string
        @param customergatewayid: customergatewayid minOccurs=0
        @type customergatewayid: string
        @param bgpasn: bgpasn minOccurs=0
        @type bgpasn: int
        @param status: status minOccurs=0
        @type status: string
        @param type: type minOccurs=0
        @type type: string
        '''
        CustomerGatewayBase.__init__(self, ipaddress=ipaddress, customergatewayid=customergatewayid, bgpasn=bgpasn, status=status, type=type)
