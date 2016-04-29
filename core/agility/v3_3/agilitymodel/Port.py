from core.agility.v3_3.agilitymodel.base.Port import PortBase
from core.agility.v3_3.agilitymodel.actions.Port import PortActions

class Port(PortBase, PortActions):
    '''
    classdocs
    '''
    def __init__(self, tenantid=None, fixedips=[], adminstateup=None, macaddress=None, deviceid=None, portid=None, deviceowner=None, status=None, network=None):
        '''
        Constructor
        @param tenantid: tenantid minOccurs=0
        @type tenantid: string
        @param fixedips: fixedips minOccurs=0 maxOccurs=unbounded
        @type fixedips: FixedIP
        @param adminstateup: adminstateup minOccurs=0
        @type adminstateup: boolean
        @param macaddress: macaddress minOccurs=0
        @type macaddress: string
        @param deviceid: deviceid minOccurs=0
        @type deviceid: string
        @param portid: portid minOccurs=0
        @type portid: string
        @param deviceowner: deviceowner minOccurs=0
        @type deviceowner: string
        @param status: status minOccurs=0
        @type status: string
        @param network: network minOccurs=0
        @type network: Link
        '''
        PortBase.__init__(self, tenantid=tenantid, fixedips=fixedips, adminstateup=adminstateup, macaddress=macaddress, deviceid=deviceid, portid=portid, deviceowner=deviceowner, status=status, network=network)
