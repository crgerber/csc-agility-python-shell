from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class EULABase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, eula='', signature='', agreedto=False, adminuser=False, readonly=False, timestamp=None, valid=False, title='', company=''):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'eula': {'native': True, 'name': 'eula', 'type': 'string'}, 'signature': {'native': True, 'name': 'signature', 'type': 'string'}, 'adminUser': {'native': True, 'name': 'adminuser', 'type': 'boolean'}, 'readOnly': {'native': True, 'name': 'readonly', 'type': 'boolean'}, 'timestamp': {'native': True, 'name': 'timestamp', 'minOccurs': '0', 'type': 'date'}, 'valid': {'native': True, 'name': 'valid', 'type': 'boolean'}, 'agreedTo': {'native': True, 'name': 'agreedto', 'type': 'boolean'}, 'title': {'native': True, 'name': 'title', 'type': 'string'}, 'company': {'native': True, 'name': 'company', 'type': 'string'}})
        self.eula = eula
        self.signature = signature
        self.agreedto = agreedto
        self.adminuser = adminuser
        self.readonly = readonly
        self.timestamp = timestamp
        self.valid = valid
        self.title = title
        self.company = company 
