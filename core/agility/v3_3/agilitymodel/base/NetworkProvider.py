from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class NetworkProviderBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, routers=[], networks=[], floatingips=[], networkprovidertype=None, networkcredentials=None, defaulttenantid=None, hostname=None):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'floatingIPs': {'maxOccurs': 'unbounded', 'native': False, 'name': 'floatingips', 'minOccurs': '0', 'type': 'Link'}, 'networks': {'maxOccurs': 'unbounded', 'native': False, 'name': 'networks', 'minOccurs': '0', 'type': 'Link'}, 'routers': {'maxOccurs': 'unbounded', 'native': False, 'name': 'routers', 'minOccurs': '0', 'type': 'Link'}, 'networkCredentials': {'native': False, 'name': 'networkcredentials', 'minOccurs': '0', 'type': 'Credential'}, 'networkProviderType': {'native': False, 'name': 'networkprovidertype', 'minOccurs': '0', 'type': 'Link'}, 'defaultTenantId': {'native': True, 'name': 'defaulttenantid', 'minOccurs': '0', 'type': 'string'}, 'hostname': {'native': True, 'name': 'hostname', 'minOccurs': '0', 'type': 'string'}})
        self.routers = routers
        self.networks = networks
        self.floatingips = floatingips
        self.networkprovidertype = networkprovidertype
        self.networkcredentials = networkcredentials
        self.defaulttenantid = defaulttenantid
        self.hostname = hostname 
