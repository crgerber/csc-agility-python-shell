from .Asset import AssetBase

class EULABase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, eula='', adminuser=False, title='', timestamp=None, company='', signature='', readonly=False, valid=False, agreedto=False):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'eula': {'type': 'string', 'name': 'eula', 'native': True}, 'adminUser': {'type': 'boolean', 'name': 'adminuser', 'native': True}, 'title': {'type': 'string', 'name': 'title', 'native': True}, 'timestamp': {'type': 'date', 'name': 'timestamp', 'minOccurs': '0', 'native': True}, 'company': {'type': 'string', 'name': 'company', 'native': True}, 'agreedTo': {'type': 'boolean', 'name': 'agreedto', 'native': True}, 'readOnly': {'type': 'boolean', 'name': 'readonly', 'native': True}, 'valid': {'type': 'boolean', 'name': 'valid', 'native': True}, 'signature': {'type': 'string', 'name': 'signature', 'native': True}})
        self.eula = eula
        self.adminuser = adminuser
        self.title = title
        self.timestamp = timestamp
        self.company = company
        self.signature = signature
        self.readonly = readonly
        self.valid = valid
        self.agreedto = agreedto 
