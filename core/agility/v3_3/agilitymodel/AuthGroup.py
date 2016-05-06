from core.agility.v3_3.agilitymodel.base.AuthGroup import AuthGroupBase
from core.agility.v3_3.agilitymodel.actions.AuthGroup import AuthGroupActions

class AuthGroup(AuthGroupBase, AuthGroupActions):
    '''
    classdocs
    '''
    def __init__(self, authserver=None, authgroupname='', mapid=None, agilityusergroups=[]):
        '''
        Constructor
        @param authserver: authserver minOccurs=0
        @type authserver: Link
        @param authgroupname: authgroupname
        @type authgroupname: string
        @param mapid: mapid minOccurs=0
        @type mapid: int
        @param agilityusergroups: agilityusergroups minOccurs=0 maxOccurs=unbounded
        @type agilityusergroups: Link
        '''
        AuthGroupBase.__init__(self, authserver=authserver, authgroupname=authgroupname, mapid=mapid, agilityusergroups=agilityusergroups)
