from base.LdapGroupList import LdapGroupListBase
from actions.LdapGroupList import LdapGroupListActions

class LdapGroupList(LdapGroupListBase, LdapGroupListActions):
    '''
    classdocs
    '''
    def __init__(self, mappings=list()):
        '''
        Constructor
        @param mappings: mappings minOccurs=0 maxOccurs=unbounded
        @type mappings: LdapGroup
        '''
        LdapGroupListBase.__init__(self, mappings=mappings)
