from core.agility.v3_3.agilitymodel.base.Credential import CredentialBase
from core.agility.v3_3.agilitymodel.actions.Credential import CredentialActions

class Credential(CredentialBase, CredentialActions):
    '''
    classdocs
    '''
    def __init__(self, certificate=None, publickey=None, managercloud=None, externallymanaged=None, credentialid=None, credentialtype=None, encrypted=None, privatekey=None, adminuser=None, secretkey=None, cloud=None, certificatename=None):
        '''
        Constructor
        @param certificate: certificate minOccurs=0
        @type certificate: hexBinary
        @param publickey: publickey minOccurs=0
        @type publickey: string
        @param managercloud: managercloud minOccurs=0
        @type managercloud: Link
        @param externallymanaged: externallymanaged minOccurs=0
        @type externallymanaged: boolean
        @param credentialid: credentialid minOccurs=0
        @type credentialid: string
        @param credentialtype: credentialtype minOccurs=0
        @type credentialtype: CredentialType
        @param encrypted: encrypted minOccurs=0
        @type encrypted: boolean
        @param privatekey: privatekey minOccurs=0
        @type privatekey: string
        @param adminuser: adminuser minOccurs=0
        @type adminuser: string
        @param secretkey: secretkey minOccurs=0
        @type secretkey: hexBinary
        @param cloud: cloud minOccurs=0
        @type cloud: Cloud
        @param certificatename: certificatename minOccurs=0
        @type certificatename: string
        '''
        CredentialBase.__init__(self, certificate=certificate, publickey=publickey, managercloud=managercloud, externallymanaged=externallymanaged, credentialid=credentialid, credentialtype=credentialtype, encrypted=encrypted, privatekey=privatekey, adminuser=adminuser, secretkey=secretkey, cloud=cloud, certificatename=certificatename)
