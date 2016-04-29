from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ProxyBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, credentials=None, proxyusage=None, authtype=None, proxytype=None, hostname=None, port=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credentials': {'native': False, 'name': 'credentials', 'minOccurs': '0', 'type': 'Credential'}, 'proxyUsage': {'native': False, 'name': 'proxyusage', 'minOccurs': '0', 'type': 'ProxyUsage'}, 'authType': {'native': False, 'name': 'authtype', 'minOccurs': '0', 'type': 'AuthType'}, 'proxyType': {'native': False, 'name': 'proxytype', 'minOccurs': '0', 'type': 'ProxyType'}, 'port': {'native': True, 'name': 'port', 'minOccurs': '0', 'type': 'int'}, 'hostname': {'native': True, 'name': 'hostname', 'minOccurs': '0', 'type': 'string'}})
        self.credentials = credentials
        self.proxyusage = proxyusage
        self.authtype = authtype
        self.proxytype = proxytype
        self.hostname = hostname
        self.port = port 
