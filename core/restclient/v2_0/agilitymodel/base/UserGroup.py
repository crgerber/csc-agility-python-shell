from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class UserGroupBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, securityRoles=list(), domain=None, users=list(), enabled=False, accessRights=list(), groups=list()):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'securityRoles': {'maxOccurs': 'unbounded', 'type': 'SecurityRole', 'name': 'securityRoles', 'minOccurs': '0', 'native': False}, 'domain': {'type': 'string', 'name': 'domain', 'minOccurs': '0', 'native': True}, 'users': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'users', 'minOccurs': '0', 'native': False}, 'enabled': {'type': 'boolean', 'name': 'enabled', 'native': True}, 'accessRights': {'maxOccurs': 'unbounded', 'type': 'AccessRight', 'name': 'accessRights', 'minOccurs': '0', 'native': False}, 'groups': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'groups', 'minOccurs': '0', 'native': False}})
        self.securityRoles = securityRoles
        self.domain = domain
        self.users = users
        self.enabled = enabled
        self.accessRights = accessRights
        self.groups = groups 
