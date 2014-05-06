from Asset import AssetBase

class AccountBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, credentials=None, enabled=None, domainname=''):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credentials': {'type': 'Credential', 'name': 'credentials', 'minOccurs': '0', 'native': False}, 'enabled': {'type': 'boolean', 'name': 'enabled', 'minOccurs': '0', 'native': True}, 'domainName': {'type': 'string', 'name': 'domainname', 'native': True}})
        self.credentials = credentials
        self.enabled = enabled
        self.domainname = domainname 
