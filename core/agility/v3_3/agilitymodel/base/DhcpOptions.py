from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class DhcpOptionsBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, cloud=None, dsnservers=[], netbiosservers=[], domainname=None, properties=[], ntpservers=[], nodetype=None, optionsid=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'dsnServers': {'name': 'dsnservers', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'netbiosServers': {'name': 'netbiosservers', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'domainName': {'name': 'domainname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'optionsId': {'name': 'optionsid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'ntpServers': {'name': 'ntpservers', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'nodeType': {'name': 'nodetype', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}})
        self.cloud = cloud
        self.dsnservers = dsnservers
        self.netbiosservers = netbiosservers
        self.domainname = domainname
        self.properties = properties
        self.ntpservers = ntpservers
        self.nodetype = nodetype
        self.optionsid = optionsid 
