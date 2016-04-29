from .base.Credential import CredentialBase
from .actions.Credential import CredentialActions

class Credential(CredentialBase, CredentialActions):
    '''
    classdocs
    '''
    def __init__(self, secretkey=None, certificatename=None, certificate=None, managercloud=None, externallymanaged=None, privatekey=None, credentialtype=None, credentialid=None, publickey=None, cloud=None):
        '''
        Constructor
        @param secretkey: secretkey minOccurs=0
        @type secretkey: hexBinary
        @param certificatename: certificatename minOccurs=0
        @type certificatename: string
        @param certificate: certificate minOccurs=0
        @type certificate: hexBinary
        @param managercloud: managercloud minOccurs=0
        @type managercloud: Link
        @param externallymanaged: externallymanaged minOccurs=0
        @type externallymanaged: boolean
        @param privatekey: privatekey minOccurs=0
        @type privatekey: string
        @param credentialtype: credentialtype minOccurs=0
        @type credentialtype: CredentialType
        @param credentialid: credentialid minOccurs=0
        @type credentialid: string
        @param publickey: publickey minOccurs=0
        @type publickey: string
        @param cloud: cloud minOccurs=0
        @type cloud: Cloud
        '''
        CredentialBase.__init__(self, secretkey=secretkey, certificatename=certificatename, certificate=certificate, managercloud=managercloud, externallymanaged=externallymanaged, privatekey=privatekey, credentialtype=credentialtype, credentialid=credentialid, publickey=publickey, cloud=cloud)
