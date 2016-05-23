from core.agility.v3_3.agilitymodel.base.Port import PortBase
from core.agility.v3_3.agilitymodel.actions.Port import PortActions

class Port(PortBase, PortActions):
    '''
    classdocs
    '''
    def __init__(self, fixedips=[], network=None, status=None, deviceid=None, adminstateup=None, portid=None, deviceowner=None, macaddress=None, tenantid=None):
        '''
        Constructor
        @param fixedips: fixedips minOccurs=0 maxOccurs=unbounded
        @type fixedips: FixedIP
        @param network: network minOccurs=0
        @type network: Link
        @param status: status minOccurs=0
        @type status: string
        @param deviceid: deviceid minOccurs=0
        @type deviceid: string
        @param adminstateup: adminstateup minOccurs=0
        @type adminstateup: boolean
        @param portid: portid minOccurs=0
        @type portid: string
        @param deviceowner: deviceowner minOccurs=0
        @type deviceowner: string
        @param macaddress: macaddress minOccurs=0
        @type macaddress: string
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        '''
        PortBase.__init__(self, fixedips=fixedips, network=network, status=status, deviceid=deviceid, adminstateup=adminstateup, portid=portid, deviceowner=deviceowner, macaddress=macaddress, tenantid=tenantid)
