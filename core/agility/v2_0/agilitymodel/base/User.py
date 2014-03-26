from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class UserBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, sshKey=None, enabled=None, accessRights=list(), groups=list(), password=None, email=None, digest=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'sshKey': {'type': 'Credential', 'name': 'sshKey', 'minOccurs': '0', 'native': False}, 'enabled': {'type': 'boolean', 'name': 'enabled', 'minOccurs': '0', 'native': True}, 'accessRights': {'maxOccurs': 'unbounded', 'type': 'AccessRight', 'name': 'accessRights', 'minOccurs': '0', 'native': False}, 'groups': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'groups', 'minOccurs': '0', 'native': False}, 'password': {'type': 'string', 'name': 'password', 'minOccurs': '0', 'native': True}, 'email': {'type': 'string', 'name': 'email', 'minOccurs': '0', 'native': True}, 'digest': {'type': 'string', 'name': 'digest', 'minOccurs': '0', 'native': True}})
        self.sshKey = sshKey
        self.enabled = enabled
        self.accessRights = accessRights
        self.groups = groups
        self.password = password
        self.email = email
        self.digest = digest 
