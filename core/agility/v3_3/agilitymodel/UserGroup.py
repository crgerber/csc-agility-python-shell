from core.agility.v3_3.agilitymodel.base.UserGroup import UserGroupBase
from core.agility.v3_3.agilitymodel.actions.UserGroup import UserGroupActions

class UserGroup(UserGroupBase, UserGroupActions):
    '''
    classdocs
    '''
    def __init__(self, users=[], accessrights=[], groups=[], enabled=False, securityroles=[], domain=None):
        '''
        Constructor
        @param users: users minOccurs=0 maxOccurs=unbounded
        @type users: Link
        @param accessrights: accessrights minOccurs=0 maxOccurs=unbounded
        @type accessrights: AccessRight
        @param groups: groups minOccurs=0 maxOccurs=unbounded
        @type groups: Link
        @param enabled: enabled
        @type enabled: boolean
        @param securityroles: securityroles minOccurs=0 maxOccurs=unbounded
        @type securityroles: SecurityRole
        @param domain: domain minOccurs=0
        @type domain: string
        '''
        UserGroupBase.__init__(self, users=users, accessrights=accessrights, groups=groups, enabled=enabled, securityroles=securityroles, domain=domain)
