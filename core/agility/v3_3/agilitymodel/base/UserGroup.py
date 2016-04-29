from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class UserGroupBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, securityroles=[], groups=[], users=[], accessrights=[], enabled=False, domain=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'securityRoles': {'maxOccurs': 'unbounded', 'native': False, 'name': 'securityroles', 'minOccurs': '0', 'type': 'SecurityRole'}, 'groups': {'maxOccurs': 'unbounded', 'native': False, 'name': 'groups', 'minOccurs': '0', 'type': 'Link'}, 'users': {'maxOccurs': 'unbounded', 'native': False, 'name': 'users', 'minOccurs': '0', 'type': 'Link'}, 'accessRights': {'maxOccurs': 'unbounded', 'native': False, 'name': 'accessrights', 'minOccurs': '0', 'type': 'AccessRight'}, 'enabled': {'native': True, 'name': 'enabled', 'type': 'boolean'}, 'domain': {'native': True, 'name': 'domain', 'minOccurs': '0', 'type': 'string'}})
        self.securityroles = securityroles
        self.groups = groups
        self.users = users
        self.accessrights = accessrights
        self.enabled = enabled
        self.domain = domain 
