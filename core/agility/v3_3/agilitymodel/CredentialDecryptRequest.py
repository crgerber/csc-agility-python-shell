from base.CredentialDecryptRequest import CredentialDecryptRequestBase
from actions.CredentialDecryptRequest import CredentialDecryptRequestActions

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
