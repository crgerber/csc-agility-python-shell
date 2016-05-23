from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class NetworkProviderBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, networkprovidertype=None, floatingips=[], defaulttenantid=None, routers=[], hostname=None, networks=[], networkcredentials=None):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'networkProviderType': {'name': 'networkprovidertype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'floatingIPs': {'name': 'floatingips', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'routers': {'name': 'routers', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'defaultTenantId': {'name': 'defaulttenantid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'hostname': {'name': 'hostname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'networks': {'name': 'networks', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'networkCredentials': {'name': 'networkcredentials', 'minOccurs': '0', 'native': False, 'type': 'Credential'}})
        self.networkprovidertype = networkprovidertype
        self.floatingips = floatingips
        self.defaulttenantid = defaulttenantid
        self.routers = routers
        self.hostname = hostname
        self.networks = networks
        self.networkcredentials = networkcredentials 
