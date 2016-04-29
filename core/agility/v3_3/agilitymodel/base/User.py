from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class UserBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, groups=[], digestexpiration=None, digest=None, accessrights=[], sshkey=None, email=None, digestiterations=None, password=None, externaluser=None, enabled=None, digestsalt=None, digestalgorithm=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'groups': {'maxOccurs': 'unbounded', 'native': False, 'name': 'groups', 'minOccurs': '0', 'type': 'Link'}, 'digestExpiration': {'native': True, 'name': 'digestexpiration', 'minOccurs': '0', 'type': 'date'}, 'digest': {'native': True, 'name': 'digest', 'minOccurs': '0', 'type': 'string'}, 'email': {'native': True, 'name': 'email', 'minOccurs': '0', 'type': 'string'}, 'accessRights': {'maxOccurs': 'unbounded', 'native': False, 'name': 'accessrights', 'minOccurs': '0', 'type': 'AccessRight'}, 'sshKey': {'native': False, 'name': 'sshkey', 'minOccurs': '0', 'type': 'Credential'}, 'digestSalt': {'native': True, 'name': 'digestsalt', 'minOccurs': '0', 'type': 'string'}, 'digestIterations': {'native': True, 'name': 'digestiterations', 'minOccurs': '0', 'type': 'int'}, 'password': {'native': True, 'name': 'password', 'minOccurs': '0', 'type': 'string'}, 'externalUser': {'native': True, 'name': 'externaluser', 'minOccurs': '0', 'type': 'boolean'}, 'enabled': {'native': True, 'name': 'enabled', 'minOccurs': '0', 'type': 'boolean'}, 'digestAlgorithm': {'native': True, 'name': 'digestalgorithm', 'minOccurs': '0', 'type': 'string'}})
        self.groups = groups
        self.digestexpiration = digestexpiration
        self.digest = digest
        self.accessrights = accessrights
        self.sshkey = sshkey
        self.email = email
        self.digestiterations = digestiterations
        self.password = password
        self.externaluser = externaluser
        self.enabled = enabled
        self.digestsalt = digestsalt
        self.digestalgorithm = digestalgorithm 
