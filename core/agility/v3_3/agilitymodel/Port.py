from base.Port import PortBase
from actions.Port import PortActions

class Port(PortBase, PortActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, macaddress=None, portid=None, network=None, adminstateup=None, deviceowner=None, tenantid=None, deviceid=None, fixedips=[]):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param macaddress: macaddress minOccurs=0
        @type macaddress: string
        @param portid: portid minOccurs=0
        @type portid: string
        @param network: network minOccurs=0
        @type network: Link
        @param adminstateup: adminstateup minOccurs=0
        @type adminstateup: boolean
        @param deviceowner: deviceowner minOccurs=0
        @type deviceowner: string
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        @param deviceid: deviceid minOccurs=0
        @type deviceid: string
        @param fixedips: fixedips minOccurs=0 maxOccurs=unbounded
        @type fixedips: FixedIP
        '''
        PortBase.__init__(self, status=status, macaddress=macaddress, portid=portid, network=network, adminstateup=adminstateup, deviceowner=deviceowner, tenantid=tenantid, deviceid=deviceid, fixedips=fixedips)
