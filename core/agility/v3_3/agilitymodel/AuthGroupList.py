from core.agility.v3_3.agilitymodel.base.AuthGroupList import AuthGroupListBase
from core.agility.v3_3.agilitymodel.actions.AuthGroupList import AuthGroupListActions

class AuthGroupList(AuthGroupListBase, AuthGroupListActions):
    '''
    classdocs
    '''
    def __init__(self, mappings=[]):
        '''
        Constructor
        @param mappings: mappings minOccurs=0 maxOccurs=unbounded
        @type mappings: AuthGroup
        '''
        AuthGroupListBase.__init__(self, mappings=mappings)
