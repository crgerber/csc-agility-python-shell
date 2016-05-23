from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class UserGroupBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, users=[], accessrights=[], groups=[], enabled=False, securityroles=[], domain=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'accessRights': {'name': 'accessrights', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AccessRight'}, 'groups': {'name': 'groups', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'enabled': {'name': 'enabled', 'native': True, 'type': 'boolean'}, 'securityRoles': {'name': 'securityroles', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'SecurityRole'}, 'domain': {'name': 'domain', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'users': {'name': 'users', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.users = users
        self.accessrights = accessrights
        self.groups = groups
        self.enabled = enabled
        self.securityroles = securityroles
        self.domain = domain 
