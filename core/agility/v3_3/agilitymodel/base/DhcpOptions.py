from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class DhcpOptionsBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, netbiosservers=[], domainname=None, nodetype=None, properties=[], optionsid=None, cloud=None, dsnservers=[], ntpservers=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'netbiosServers': {'maxOccurs': 'unbounded', 'native': True, 'name': 'netbiosservers', 'minOccurs': '0', 'type': 'string'}, 'domainName': {'native': True, 'name': 'domainname', 'minOccurs': '0', 'type': 'string'}, 'dsnServers': {'maxOccurs': 'unbounded', 'native': True, 'name': 'dsnservers', 'minOccurs': '0', 'type': 'string'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'optionsId': {'native': True, 'name': 'optionsid', 'minOccurs': '0', 'type': 'string'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'nodeType': {'native': True, 'name': 'nodetype', 'minOccurs': '0', 'type': 'int'}, 'ntpServers': {'maxOccurs': 'unbounded', 'native': True, 'name': 'ntpservers', 'minOccurs': '0', 'type': 'string'}})
        self.netbiosservers = netbiosservers
        self.domainname = domainname
        self.nodetype = nodetype
        self.properties = properties
        self.optionsid = optionsid
        self.cloud = cloud
        self.dsnservers = dsnservers
        self.ntpservers = ntpservers 
