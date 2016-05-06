from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class UserBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, digestiterations=None, sshkey=None, digestalgorithm=None, digestsalt=None, enabled=None, accessrights=[], externaluser=None, groups=[], digestexpiration=None, password=None, email=None, digest=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'digestIterations': {'type': 'int', 'name': 'digestiterations', 'minOccurs': '0', 'native': True}, 'sshKey': {'type': 'Credential', 'name': 'sshkey', 'minOccurs': '0', 'native': False}, 'digestAlgorithm': {'type': 'string', 'name': 'digestalgorithm', 'minOccurs': '0', 'native': True}, 'digestSalt': {'type': 'string', 'name': 'digestsalt', 'minOccurs': '0', 'native': True}, 'enabled': {'type': 'boolean', 'name': 'enabled', 'minOccurs': '0', 'native': True}, 'accessRights': {'maxOccurs': 'unbounded', 'type': 'AccessRight', 'name': 'accessrights', 'minOccurs': '0', 'native': False}, 'externalUser': {'type': 'boolean', 'name': 'externaluser', 'minOccurs': '0', 'native': True}, 'groups': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'groups', 'minOccurs': '0', 'native': False}, 'digestExpiration': {'type': 'date', 'name': 'digestexpiration', 'minOccurs': '0', 'native': True}, 'password': {'type': 'string', 'name': 'password', 'minOccurs': '0', 'native': True}, 'email': {'type': 'string', 'name': 'email', 'minOccurs': '0', 'native': True}, 'digest': {'type': 'string', 'name': 'digest', 'minOccurs': '0', 'native': True}})
        self.digestiterations = digestiterations
        self.sshkey = sshkey
        self.digestalgorithm = digestalgorithm
        self.digestsalt = digestsalt
        self.enabled = enabled
        self.accessrights = accessrights
        self.externaluser = externaluser
        self.groups = groups
        self.digestexpiration = digestexpiration
        self.password = password
        self.email = email
        self.digest = digest 
