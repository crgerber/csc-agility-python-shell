from Asset import AssetBase

class DhcpOptionsBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, nodeType=None, domainName=None, ntpServers=list(), cloud=None, dsnServers=list(), optionsId=None, properties=list(), netbiosServers=list()):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'nodeType': {'type': 'int', 'name': 'nodeType', 'minOccurs': '0', 'native': True}, 'domainName': {'type': 'string', 'name': 'domainName', 'minOccurs': '0', 'native': True}, 'ntpServers': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'ntpServers', 'minOccurs': '0', 'native': True}, 'netbiosServers': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'netbiosServers', 'minOccurs': '0', 'native': True}, 'dsnServers': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'dsnServers', 'minOccurs': '0', 'native': True}, 'optionsId': {'type': 'string', 'name': 'optionsId', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.nodeType = nodeType
        self.domainName = domainName
        self.ntpServers = ntpServers
        self.cloud = cloud
        self.dsnServers = dsnServers
        self.optionsId = optionsId
        self.properties = properties
        self.netbiosServers = netbiosServers 
