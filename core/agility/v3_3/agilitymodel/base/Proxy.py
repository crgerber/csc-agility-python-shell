from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ProxyBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, credentials=None, proxyusage=None, authtype=None, port=None, hostname=None, proxytype=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credentials': {'name': 'credentials', 'minOccurs': '0', 'native': False, 'type': 'Credential'}, 'proxyUsage': {'name': 'proxyusage', 'minOccurs': '0', 'native': False, 'type': 'ProxyUsage'}, 'authType': {'name': 'authtype', 'minOccurs': '0', 'native': False, 'type': 'AuthType'}, 'port': {'name': 'port', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'hostname': {'name': 'hostname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'proxyType': {'name': 'proxytype', 'minOccurs': '0', 'native': False, 'type': 'ProxyType'}})
        self.credentials = credentials
        self.proxyusage = proxyusage
        self.authtype = authtype
        self.port = port
        self.hostname = hostname
        self.proxytype = proxytype 
