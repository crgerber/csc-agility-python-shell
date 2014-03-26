from core.agility.v2_0.agilitymodel.base.UserGroup import UserGroupBase
from core.agility.v2_0.agilitymodel.actions.UserGroup import UserGroupActions

class UserGroup(UserGroupBase, UserGroupActions):
    '''
    classdocs
    '''
    def __init__(self, securityRoles=list(), domain=None, users=list(), enabled=False, accessRights=list(), groups=list()):
        '''
        Constructor
        @param securityRoles: securityRoles minOccurs=0 maxOccurs=unbounded
        @type securityRoles: SecurityRole
        @param domain: domain minOccurs=0
        @type domain: string
        @param users: users minOccurs=0 maxOccurs=unbounded
        @type users: Link
        @param enabled: enabled
        @type enabled: boolean
        @param accessRights: accessRights minOccurs=0 maxOccurs=unbounded
        @type accessRights: AccessRight
        @param groups: groups minOccurs=0 maxOccurs=unbounded
        @type groups: Link
        '''
        UserGroupBase.__init__(self, securityRoles=securityRoles, domain=domain, users=users, enabled=enabled, accessRights=accessRights, groups=groups)
