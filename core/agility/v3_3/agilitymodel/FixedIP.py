from core.agility.v3_3.agilitymodel.base.FixedIP import FixedIPBase
from core.agility.v3_3.agilitymodel.actions.FixedIP import FixedIPActions

class FixedIP(FixedIPBase, FixedIPActions):
    '''
    classdocs
    '''
    def __init__(self, ipaddress=None, subnet=None, id=None):
        '''
        Constructor
        @param ipaddress: ipaddress minOccurs=0
        @type ipaddress: string
        @param subnet: subnet minOccurs=0
        @type subnet: Link
        @param id: id minOccurs=0
        @type id: int
        '''
        FixedIPBase.__init__(self, ipaddress=ipaddress, subnet=subnet, id=id)
