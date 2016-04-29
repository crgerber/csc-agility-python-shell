from core.agility.v3_3.agilitymodel.base.AccessList import AccessListBase
from core.agility.v3_3.agilitymodel.actions.AccessList import AccessListActions

class AccessList(AccessListBase, AccessListActions):
    '''
    classdocs
    '''
    def __init__(self, direction=None, protocols=[]):
        '''
        Constructor
        @param direction: direction minOccurs=0
        @type direction: AccessListDirection
        @param protocols: protocols minOccurs=0 maxOccurs=unbounded
        @type protocols: Protocol
        '''
        AccessListBase.__init__(self, direction=direction, protocols=protocols)
