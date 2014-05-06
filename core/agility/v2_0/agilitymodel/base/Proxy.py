from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class ProxyBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, proxyType=None, authType=None, proxyUsage=None, hostname=None, credentials=None, port=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'proxyType': {'type': 'ProxyType', 'name': 'proxyType', 'minOccurs': '0', 'native': False}, 'authType': {'type': 'AuthType', 'name': 'authType', 'minOccurs': '0', 'native': False}, 'proxyUsage': {'type': 'ProxyUsage', 'name': 'proxyUsage', 'minOccurs': '0', 'native': False}, 'hostname': {'type': 'string', 'name': 'hostname', 'minOccurs': '0', 'native': True}, 'credentials': {'type': 'Credential', 'name': 'credentials', 'minOccurs': '0', 'native': False}, 'port': {'type': 'int', 'name': 'port', 'minOccurs': '0', 'native': True}})
        self.proxyType = proxyType
        self.authType = authType
        self.proxyUsage = proxyUsage
        self.hostname = hostname
        self.credentials = credentials
        self.port = port 
