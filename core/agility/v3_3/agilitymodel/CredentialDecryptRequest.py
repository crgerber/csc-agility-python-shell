from core.agility.v3_3.agilitymodel.base.CredentialDecryptRequest import CredentialDecryptRequestBase
from core.agility.v3_3.agilitymodel.actions.CredentialDecryptRequest import CredentialDecryptRequestActions

class CredentialDecryptRequest(CredentialDecryptRequestBase, CredentialDecryptRequestActions):
    '''
    classdocs
    '''
    def __init__(self, credentialid=None):
        '''
        Constructor
        @param credentialid: credentialid
        @type credentialid: int
        '''
        CredentialDecryptRequestBase.__init__(self, credentialid=credentialid)
