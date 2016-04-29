from core.agility.v3_3.agilitymodel.base.LdapGroup import LdapGroupBase
from core.agility.v3_3.agilitymodel.actions.LdapGroup import LdapGroupActions

class LdapGroup(LdapGroupBase, LdapGroupActions):
    '''
    classdocs
    '''
    def __init__(self, agilitygroupname='', ldapgroupname='', mapid=None):
        '''
        Constructor
        @param agilitygroupname: agilitygroupname
        @type agilitygroupname: string
        @param ldapgroupname: ldapgroupname
        @type ldapgroupname: string
        @param mapid: mapid minOccurs=0
        @type mapid: int
        '''
        LdapGroupBase.__init__(self, agilitygroupname=agilitygroupname, ldapgroupname=ldapgroupname, mapid=mapid)
