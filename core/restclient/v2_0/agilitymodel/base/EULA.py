from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class EULABase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, eula='', adminUser=False, title='', timestamp=None, company='', signature='', readOnly=False, valid=False, agreedTo=False):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'eula': {'type': 'string', 'name': 'eula', 'native': True}, 'adminUser': {'type': 'boolean', 'name': 'adminUser', 'native': True}, 'title': {'type': 'string', 'name': 'title', 'native': True}, 'timestamp': {'type': 'date', 'name': 'timestamp', 'minOccurs': '0', 'native': True}, 'company': {'type': 'string', 'name': 'company', 'native': True}, 'agreedTo': {'type': 'boolean', 'name': 'agreedTo', 'native': True}, 'readOnly': {'type': 'boolean', 'name': 'readOnly', 'native': True}, 'valid': {'type': 'boolean', 'name': 'valid', 'native': True}, 'signature': {'type': 'string', 'name': 'signature', 'native': True}})
        self.eula = eula
        self.adminUser = adminUser
        self.title = title
        self.timestamp = timestamp
        self.company = company
        self.signature = signature
        self.readOnly = readOnly
        self.valid = valid
        self.agreedTo = agreedTo 
