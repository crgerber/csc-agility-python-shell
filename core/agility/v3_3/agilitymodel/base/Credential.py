from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class CredentialBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, managercloud=None, credentialtype=None, secretkey=None, privatekey=None, adminuser=None, encrypted=None, certificatename=None, cloud=None, publickey=None, credentialid=None, externallymanaged=None, certificate=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'managerCloud': {'name': 'managercloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'credentialType': {'name': 'credentialtype', 'minOccurs': '0', 'native': False, 'type': 'CredentialType'}, 'secretKey': {'name': 'secretkey', 'minOccurs': '0', 'native': True, 'type': 'hexBinary'}, 'privateKey': {'name': 'privatekey', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'credentialId': {'name': 'credentialid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'encrypted': {'name': 'encrypted', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'certificateName': {'name': 'certificatename', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Cloud'}, 'publicKey': {'name': 'publickey', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'adminUser': {'name': 'adminuser', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'externallyManaged': {'name': 'externallymanaged', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'certificate': {'name': 'certificate', 'minOccurs': '0', 'native': True, 'type': 'hexBinary'}})
        self.managercloud = managercloud
        self.credentialtype = credentialtype
        self.secretkey = secretkey
        self.privatekey = privatekey
        self.adminuser = adminuser
        self.encrypted = encrypted
        self.certificatename = certificatename
        self.cloud = cloud
        self.publickey = publickey
        self.credentialid = credentialid
        self.externallymanaged = externallymanaged
        self.certificate = certificate 
