from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class UserBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, password=None, digestiterations=None, accessrights=[], sshkey=None, digestsalt=None, enabled=None, externaluser=None, digestalgorithm=None, email=None, digest=None, digestexpiration=None, groups=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'password': {'name': 'password', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'digestIterations': {'name': 'digestiterations', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'accessRights': {'name': 'accessrights', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AccessRight'}, 'sshKey': {'name': 'sshkey', 'minOccurs': '0', 'native': False, 'type': 'Credential'}, 'digestSalt': {'name': 'digestsalt', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'enabled': {'name': 'enabled', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'externalUser': {'name': 'externaluser', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'digestAlgorithm': {'name': 'digestalgorithm', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'email': {'name': 'email', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'digest': {'name': 'digest', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'digestExpiration': {'name': 'digestexpiration', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'groups': {'name': 'groups', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.password = password
        self.digestiterations = digestiterations
        self.accessrights = accessrights
        self.sshkey = sshkey
        self.digestsalt = digestsalt
        self.enabled = enabled
        self.externaluser = externaluser
        self.digestalgorithm = digestalgorithm
        self.email = email
        self.digest = digest
        self.digestexpiration = digestexpiration
        self.groups = groups 
