from core.agility.v3_3.agilitymodel.base.LdapGroup import LdapGroupBase
from core.agility.v3_3.agilitymodel.actions.LdapGroup import LdapGroupActions

class LdapGroup(LdapGroupBase, LdapGroupActions):
    '''
    classdocs
    '''
    def __init__(self, mapid=None, ldapgroupname='', agilitygroupname=''):
        '''
        Constructor
        @param mapid: mapid minOccurs=0
        @type mapid: int
        @param ldapgroupname: ldapgroupname
        @type ldapgroupname: string
        @param agilitygroupname: agilitygroupname
        @type agilitygroupname: string
        '''
        LdapGroupBase.__init__(self, mapid=mapid, ldapgroupname=ldapgroupname, agilitygroupname=agilitygroupname)
