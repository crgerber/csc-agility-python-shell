from core.agility.v3_3.agilitymodel.base.AuthGroup import AuthGroupBase
from core.agility.v3_3.agilitymodel.actions.AuthGroup import AuthGroupActions

class AuthGroup(AuthGroupBase, AuthGroupActions):
    '''
    classdocs
    '''
    def __init__(self, authgroupname='', authserver=None, mapid=None, agilityusergroups=[]):
        '''
        Constructor
        @param authgroupname: authgroupname
        @type authgroupname: string
        @param authserver: authserver minOccurs=0
        @type authserver: Link
        @param mapid: mapid minOccurs=0
        @type mapid: int
        @param agilityusergroups: agilityusergroups minOccurs=0 maxOccurs=unbounded
        @type agilityusergroups: Link
        '''
        AuthGroupBase.__init__(self, authgroupname=authgroupname, authserver=authserver, mapid=mapid, agilityusergroups=agilityusergroups)
