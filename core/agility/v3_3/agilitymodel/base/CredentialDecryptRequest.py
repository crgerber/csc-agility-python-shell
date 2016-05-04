from ApiRequest import ApiRequestBase

class CredentialDecryptRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, credentialid=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credentialId': {'type': 'int', 'name': 'credentialid', 'native': True}})
        self.credentialid = credentialid 
