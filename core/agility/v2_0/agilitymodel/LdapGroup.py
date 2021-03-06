from core.agility.v2_0.agilitymodel.base.LdapGroup import LdapGroupBase
from core.agility.v2_0.agilitymodel.actions.LdapGroup import LdapGroupActions

class LdapGroup(LdapGroupBase, LdapGroupActions):
    '''
    classdocs
    '''
    def __init__(self, mapId=None, ldapGroupName='', agilityGroupName=''):
        '''
        Constructor
        @param mapId: mapId minOccurs=0
        @type mapId: int
        @param ldapGroupName: ldapGroupName
        @type ldapGroupName: string
        @param agilityGroupName: agilityGroupName
        @type agilityGroupName: string
        '''
        LdapGroupBase.__init__(self, mapId=mapId, ldapGroupName=ldapGroupName, agilityGroupName=agilityGroupName)
