from core.agility.v3_3.agilitymodel.base.UserGroup import UserGroupBase
from core.agility.v3_3.agilitymodel.actions.UserGroup import UserGroupActions

class UserGroup(UserGroupBase, UserGroupActions):
    '''
    classdocs
    '''
    def __init__(self, securityroles=[], groups=[], users=[], accessrights=[], enabled=False, domain=None):
        '''
        Constructor
        @param securityroles: securityroles minOccurs=0 maxOccurs=unbounded
        @type securityroles: SecurityRole
        @param groups: groups minOccurs=0 maxOccurs=unbounded
        @type groups: Link
        @param users: users minOccurs=0 maxOccurs=unbounded
        @type users: Link
        @param accessrights: accessrights minOccurs=0 maxOccurs=unbounded
        @type accessrights: AccessRight
        @param enabled: enabled
        @type enabled: boolean
        @param domain: domain minOccurs=0
        @type domain: string
        '''
        UserGroupBase.__init__(self, securityroles=securityroles, groups=groups, users=users, accessrights=accessrights, enabled=enabled, domain=domain)
