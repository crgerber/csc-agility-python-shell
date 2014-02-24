from base.Credential import CredentialBase
from actions.Credential import CredentialActions

class Credential(CredentialBase, CredentialActions):
    '''
    classdocs
    '''
    def __init__(self, certificateName=None, certificate=None, managerCloud=None, externallyManaged=None, privateKey=None, credentialType=None, secretKey=None, publicKey=None, cloud=None):
        '''
        Constructor
        @param certificateName: certificateName minOccurs=0
        @type certificateName: string
        @param certificate: certificate minOccurs=0
        @type certificate: hexBinary
        @param managerCloud: managerCloud minOccurs=0
        @type managerCloud: Link
        @param externallyManaged: externallyManaged minOccurs=0
        @type externallyManaged: boolean
        @param privateKey: privateKey minOccurs=0
        @type privateKey: string
        @param credentialType: credentialType minOccurs=0
        @type credentialType: CredentialType
        @param secretKey: secretKey minOccurs=0
        @type secretKey: hexBinary
        @param publicKey: publicKey minOccurs=0
        @type publicKey: string
        @param cloud: cloud minOccurs=0
        @type cloud: Cloud
        '''
        CredentialBase.__init__(self, certificateName=certificateName, certificate=certificate, managerCloud=managerCloud, externallyManaged=externallyManaged, privateKey=privateKey, credentialType=credentialType, secretKey=secretKey, publicKey=publicKey, cloud=cloud)
