from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class DhcpOptionsBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, nodetype=None, domainname=None, ntpservers=[], cloud=None, dsnservers=[], optionsid=None, properties=[], netbiosservers=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'nodeType': {'type': 'int', 'name': 'nodetype', 'minOccurs': '0', 'native': True}, 'domainName': {'type': 'string', 'name': 'domainname', 'minOccurs': '0', 'native': True}, 'ntpServers': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'ntpservers', 'minOccurs': '0', 'native': True}, 'netbiosServers': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'netbiosservers', 'minOccurs': '0', 'native': True}, 'dsnServers': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'dsnservers', 'minOccurs': '0', 'native': True}, 'optionsId': {'type': 'string', 'name': 'optionsid', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.nodetype = nodetype
        self.domainname = domainname
        self.ntpservers = ntpservers
        self.cloud = cloud
        self.dsnservers = dsnservers
        self.optionsid = optionsid
        self.properties = properties
        self.netbiosservers = netbiosservers 
