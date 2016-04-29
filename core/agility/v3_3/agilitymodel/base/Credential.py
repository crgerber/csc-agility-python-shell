from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class CredentialBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, certificate=None, publickey=None, managercloud=None, externallymanaged=None, credentialid=None, credentialtype=None, encrypted=None, privatekey=None, adminuser=None, secretkey=None, cloud=None, certificatename=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'certificate': {'native': True, 'name': 'certificate', 'minOccurs': '0', 'type': 'hexBinary'}, 'publicKey': {'native': True, 'name': 'publickey', 'minOccurs': '0', 'type': 'string'}, 'managerCloud': {'native': False, 'name': 'managercloud', 'minOccurs': '0', 'type': 'Link'}, 'externallyManaged': {'native': True, 'name': 'externallymanaged', 'minOccurs': '0', 'type': 'boolean'}, 'credentialId': {'native': True, 'name': 'credentialid', 'minOccurs': '0', 'type': 'string'}, 'credentialType': {'native': False, 'name': 'credentialtype', 'minOccurs': '0', 'type': 'CredentialType'}, 'encrypted': {'native': True, 'name': 'encrypted', 'minOccurs': '0', 'type': 'boolean'}, 'privateKey': {'native': True, 'name': 'privatekey', 'minOccurs': '0', 'type': 'string'}, 'adminUser': {'native': True, 'name': 'adminuser', 'minOccurs': '0', 'type': 'string'}, 'secretKey': {'native': True, 'name': 'secretkey', 'minOccurs': '0', 'type': 'hexBinary'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Cloud'}, 'certificateName': {'native': True, 'name': 'certificatename', 'minOccurs': '0', 'type': 'string'}})
        self.certificate = certificate
        self.publickey = publickey
        self.managercloud = managercloud
        self.externallymanaged = externallymanaged
        self.credentialid = credentialid
        self.credentialtype = credentialtype
        self.encrypted = encrypted
        self.privatekey = privatekey
        self.adminuser = adminuser
        self.secretkey = secretkey
        self.cloud = cloud
        self.certificatename = certificatename 
