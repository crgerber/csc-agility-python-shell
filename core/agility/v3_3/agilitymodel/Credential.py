from core.agility.v3_3.agilitymodel.base.Credential import CredentialBase
from core.agility.v3_3.agilitymodel.actions.Credential import CredentialActions

class Credential(CredentialBase, CredentialActions):
    '''
    classdocs
    '''
    def __init__(self, managercloud=None, credentialtype=None, secretkey=None, privatekey=None, adminuser=None, encrypted=None, certificatename=None, cloud=None, publickey=None, credentialid=None, externallymanaged=None, certificate=None):
        '''
        Constructor
        @param managercloud: managercloud minOccurs=0
        @type managercloud: Link
        @param credentialtype: credentialtype minOccurs=0
        @type credentialtype: CredentialType
        @param secretkey: secretkey minOccurs=0
        @type secretkey: hexBinary
        @param privatekey: privatekey minOccurs=0
        @type privatekey: string
        @param adminuser: adminuser minOccurs=0
        @type adminuser: string
        @param encrypted: encrypted minOccurs=0
        @type encrypted: boolean
        @param certificatename: certificatename minOccurs=0
        @type certificatename: string
        @param cloud: cloud minOccurs=0
        @type cloud: Cloud
        @param publickey: publickey minOccurs=0
        @type publickey: string
        @param credentialid: credentialid minOccurs=0
        @type credentialid: string
        @param externallymanaged: externallymanaged minOccurs=0
        @type externallymanaged: boolean
        @param certificate: certificate minOccurs=0
        @type certificate: hexBinary
        '''
        CredentialBase.__init__(self, managercloud=managercloud, credentialtype=credentialtype, secretkey=secretkey, privatekey=privatekey, adminuser=adminuser, encrypted=encrypted, certificatename=certificatename, cloud=cloud, publickey=publickey, credentialid=credentialid, externallymanaged=externallymanaged, certificate=certificate)
