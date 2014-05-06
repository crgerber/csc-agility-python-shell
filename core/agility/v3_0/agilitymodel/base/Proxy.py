from core.agility.v3_0.agilitymodel.base.Asset import AssetBase

class ProxyBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, proxytype=None, authtype=None, proxyusage=None, hostname=None, credentials=None, port=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'proxyType': {'type': 'ProxyType', 'name': 'proxytype', 'minOccurs': '0', 'native': False}, 'authType': {'type': 'AuthType', 'name': 'authtype', 'minOccurs': '0', 'native': False}, 'proxyUsage': {'type': 'ProxyUsage', 'name': 'proxyusage', 'minOccurs': '0', 'native': False}, 'hostname': {'type': 'string', 'name': 'hostname', 'minOccurs': '0', 'native': True}, 'credentials': {'type': 'Credential', 'name': 'credentials', 'minOccurs': '0', 'native': False}, 'port': {'type': 'int', 'name': 'port', 'minOccurs': '0', 'native': True}})
        self.proxytype = proxytype
        self.authtype = authtype
        self.proxyusage = proxyusage
        self.hostname = hostname
        self.credentials = credentials
        self.port = port 
