from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class UserGroupBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, securityroles=[], domain=None, users=[], enabled=False, accessrights=[], groups=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'securityRoles': {'maxOccurs': 'unbounded', 'type': 'SecurityRole', 'name': 'securityroles', 'minOccurs': '0', 'native': False}, 'domain': {'type': 'string', 'name': 'domain', 'minOccurs': '0', 'native': True}, 'users': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'users', 'minOccurs': '0', 'native': False}, 'enabled': {'type': 'boolean', 'name': 'enabled', 'native': True}, 'accessRights': {'maxOccurs': 'unbounded', 'type': 'AccessRight', 'name': 'accessrights', 'minOccurs': '0', 'native': False}, 'groups': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'groups', 'minOccurs': '0', 'native': False}})
        self.securityroles = securityroles
        self.domain = domain
        self.users = users
        self.enabled = enabled
        self.accessrights = accessrights
        self.groups = groups 
