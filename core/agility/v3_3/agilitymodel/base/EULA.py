from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class EULABase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, timestamp=None, title='', valid=False, readonly=False, signature='', agreedto=False, eula='', adminuser=False, company=''):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'timestamp': {'name': 'timestamp', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'title': {'name': 'title', 'native': True, 'type': 'string'}, 'adminUser': {'name': 'adminuser', 'native': True, 'type': 'boolean'}, 'readOnly': {'name': 'readonly', 'native': True, 'type': 'boolean'}, 'signature': {'name': 'signature', 'native': True, 'type': 'string'}, 'valid': {'name': 'valid', 'native': True, 'type': 'boolean'}, 'eula': {'name': 'eula', 'native': True, 'type': 'string'}, 'agreedTo': {'name': 'agreedto', 'native': True, 'type': 'boolean'}, 'company': {'name': 'company', 'native': True, 'type': 'string'}})
        self.timestamp = timestamp
        self.title = title
        self.valid = valid
        self.readonly = readonly
        self.signature = signature
        self.agreedto = agreedto
        self.eula = eula
        self.adminuser = adminuser
        self.company = company 
