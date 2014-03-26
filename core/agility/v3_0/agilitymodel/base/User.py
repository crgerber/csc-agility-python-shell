from core.agility.v3_0.agilitymodel.base.Asset import AssetBase

class UserBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, sshkey=None, enabled=None, accessrights=[], uselocalauth=None, groups=[], password=None, email=None, digest=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'sshKey': {'type': 'Credential', 'name': 'sshkey', 'minOccurs': '0', 'native': False}, 'enabled': {'type': 'boolean', 'name': 'enabled', 'minOccurs': '0', 'native': True}, 'accessRights': {'maxOccurs': 'unbounded', 'type': 'AccessRight', 'name': 'accessrights', 'minOccurs': '0', 'native': False}, 'useLocalAuth': {'type': 'boolean', 'name': 'uselocalauth', 'minOccurs': '0', 'native': True}, 'groups': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'groups', 'minOccurs': '0', 'native': False}, 'password': {'type': 'string', 'name': 'password', 'minOccurs': '0', 'native': True}, 'email': {'type': 'string', 'name': 'email', 'minOccurs': '0', 'native': True}, 'digest': {'type': 'string', 'name': 'digest', 'minOccurs': '0', 'native': True}})
        self.sshkey = sshkey
        self.enabled = enabled
        self.accessrights = accessrights
        self.uselocalauth = uselocalauth
        self.groups = groups
        self.password = password
        self.email = email
        self.digest = digest 
