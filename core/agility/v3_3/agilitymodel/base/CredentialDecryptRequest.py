from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class CredentialDecryptRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, credentialid=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credentialId': {'native': True, 'name': 'credentialid', 'type': 'int'}})
        self.credentialid = credentialid 
