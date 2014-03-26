from core.agility.v3_0.agilitymodel.base.UserGroup import UserGroupBase
from core.agility.v3_0.agilitymodel.actions.UserGroup import UserGroupActions

class UserGroup(UserGroupBase, UserGroupActions):
    '''
    classdocs
    '''
    def __init__(self, securityroles=[], domain=None, users=[], enabled=False, accessrights=[], groups=[]):
        '''
        Constructor
        @param securityroles: securityroles minOccurs=0 maxOccurs=unbounded
        @type securityroles: SecurityRole
        @param domain: domain minOccurs=0
        @type domain: string
        @param users: users minOccurs=0 maxOccurs=unbounded
        @type users: Link
        @param enabled: enabled
        @type enabled: boolean
        @param accessrights: accessrights minOccurs=0 maxOccurs=unbounded
        @type accessrights: AccessRight
        @param groups: groups minOccurs=0 maxOccurs=unbounded
        @type groups: Link
        '''
        UserGroupBase.__init__(self, securityroles=securityroles, domain=domain, users=users, enabled=enabled, accessrights=accessrights, groups=groups)
