from base.AuthGroupList import AuthGroupListBase
from actions.AuthGroupList import AuthGroupListActions

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
