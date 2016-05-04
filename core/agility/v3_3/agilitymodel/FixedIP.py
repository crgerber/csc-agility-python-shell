from base.FixedIP import FixedIPBase
from actions.FixedIP import FixedIPActions

class FixedIP(FixedIPBase, FixedIPActions):
    '''
    classdocs
    '''
    def __init__(self, subnet=None, ipaddress=None, id=None):
        '''
        Constructor
        @param subnet: subnet minOccurs=0
        @type subnet: Link
        @param ipaddress: ipaddress minOccurs=0
        @type ipaddress: string
        @param id: id minOccurs=0
        @type id: int
        '''
        FixedIPBase.__init__(self, subnet=subnet, ipaddress=ipaddress, id=id)
