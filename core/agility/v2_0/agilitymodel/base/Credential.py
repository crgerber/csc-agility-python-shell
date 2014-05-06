from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class CredentialBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, certificateName=None, certificate=None, managerCloud=None, externallyManaged=None, privateKey=None, credentialType=None, secretKey=None, publicKey=None, cloud=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'certificateName': {'type': 'string', 'name': 'certificateName', 'minOccurs': '0', 'native': True}, 'certificate': {'type': 'hexBinary', 'name': 'certificate', 'minOccurs': '0', 'native': True}, 'managerCloud': {'type': 'Link', 'name': 'managerCloud', 'minOccurs': '0', 'native': False}, 'externallyManaged': {'type': 'boolean', 'name': 'externallyManaged', 'minOccurs': '0', 'native': True}, 'privateKey': {'type': 'string', 'name': 'privateKey', 'minOccurs': '0', 'native': True}, 'credentialType': {'type': 'CredentialType', 'name': 'credentialType', 'minOccurs': '0', 'native': False}, 'secretKey': {'type': 'hexBinary', 'name': 'secretKey', 'minOccurs': '0', 'native': True}, 'publicKey': {'type': 'string', 'name': 'publicKey', 'minOccurs': '0', 'native': True}, 'cloud': {'type': 'Cloud', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.certificateName = certificateName
        self.certificate = certificate
        self.managerCloud = managerCloud
        self.externallyManaged = externallyManaged
        self.privateKey = privateKey
        self.credentialType = credentialType
        self.secretKey = secretKey
        self.publicKey = publicKey
        self.cloud = cloud 
