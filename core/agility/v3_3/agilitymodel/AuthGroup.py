from core.agility.v3_3.agilitymodel.base.AuthGroup import AuthGroupBase
from core.agility.v3_3.agilitymodel.actions.AuthGroup import AuthGroupActions

class AuthGroup(AuthGroupBase, AuthGroupActions):
    '''
    classdocs
    '''
    def __init__(self, mapid=None, agilityusergroups=[], authserver=None, authgroupname=''):
        '''
        Constructor
        @param mapid: mapid minOccurs=0
        @type mapid: int
        @param agilityusergroups: agilityusergroups minOccurs=0 maxOccurs=unbounded
        @type agilityusergroups: Link
        @param authserver: authserver minOccurs=0
        @type authserver: Link
        @param authgroupname: authgroupname
        @type authgroupname: string
        '''
        AuthGroupBase.__init__(self, mapid=mapid, agilityusergroups=agilityusergroups, authserver=authserver, authgroupname=authgroupname)
