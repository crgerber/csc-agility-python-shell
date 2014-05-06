from core.agility.v3_0.agilitymodel.base.LdapGroupList import LdapGroupListBase
from core.agility.v3_0.agilitymodel.actions.LdapGroupList import LdapGroupListActions

class LdapGroupList(LdapGroupListBase, LdapGroupListActions):
    '''
    classdocs
    '''
    def __init__(self, mappings=[]):
        '''
        Constructor
        @param mappings: mappings minOccurs=0 maxOccurs=unbounded
        @type mappings: LdapGroup
        '''
        LdapGroupListBase.__init__(self, mappings=mappings)
