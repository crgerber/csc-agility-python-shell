from core.agility.v3_3.agilitymodel.base.FixedIP import FixedIPBase
from core.agility.v3_3.agilitymodel.actions.FixedIP import FixedIPActions

class FixedIP(FixedIPBase, FixedIPActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, subnet=None, ipaddress=None):
        '''
        Constructor
        @param id: id minOccurs=0
        @type id: int
        @param subnet: subnet minOccurs=0
        @type subnet: Link
        @param ipaddress: ipaddress minOccurs=0
        @type ipaddress: string
        '''
        FixedIPBase.__init__(self, id=id, subnet=subnet, ipaddress=ipaddress)
