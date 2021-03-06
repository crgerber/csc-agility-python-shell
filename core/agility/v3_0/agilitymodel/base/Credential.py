from core.agility.v3_0.agilitymodel.base.Item import ItemBase

class CredentialBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, secretkey=None, certificatename=None, certificate=None, managercloud=None, externallymanaged=None, privatekey=None, credentialtype=None, credentialid=None, publickey=None, cloud=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credentialId': {'type': 'string', 'name': 'credentialid', 'minOccurs': '0', 'native': True}, 'certificateName': {'type': 'string', 'name': 'certificatename', 'minOccurs': '0', 'native': True}, 'certificate': {'type': 'hexBinary', 'name': 'certificate', 'minOccurs': '0', 'native': True}, 'managerCloud': {'type': 'Link', 'name': 'managercloud', 'minOccurs': '0', 'native': False}, 'externallyManaged': {'type': 'boolean', 'name': 'externallymanaged', 'minOccurs': '0', 'native': True}, 'privateKey': {'type': 'string', 'name': 'privatekey', 'minOccurs': '0', 'native': True}, 'credentialType': {'type': 'CredentialType', 'name': 'credentialtype', 'minOccurs': '0', 'native': False}, 'secretKey': {'type': 'hexBinary', 'name': 'secretkey', 'minOccurs': '0', 'native': True}, 'publicKey': {'type': 'string', 'name': 'publickey', 'minOccurs': '0', 'native': True}, 'cloud': {'type': 'Cloud', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.secretkey = secretkey
        self.certificatename = certificatename
        self.certificate = certificate
        self.managercloud = managercloud
        self.externallymanaged = externallymanaged
        self.privatekey = privatekey
        self.credentialtype = credentialtype
        self.credentialid = credentialid
        self.publickey = publickey
        self.cloud = cloud 
