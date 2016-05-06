from core.agility.v3_3.agilitymodel.base.SdnItem import SdnItemBase

class NetworkProviderBase(SdnItemBase):
    '''
    classdocs
    '''
    def __init__(self, networkcredentials=None, defaulttenantid=None, routers=[], hostname=None, networkprovidertype=None, networks=[], floatingips=[]):
        SdnItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'networkCredentials': {'type': 'Credential', 'name': 'networkcredentials', 'minOccurs': '0', 'native': False}, 'defaultTenantId': {'type': 'string', 'name': 'defaulttenantid', 'minOccurs': '0', 'native': True}, 'routers': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'routers', 'minOccurs': '0', 'native': False}, 'hostname': {'type': 'string', 'name': 'hostname', 'minOccurs': '0', 'native': True}, 'networkProviderType': {'type': 'Link', 'name': 'networkprovidertype', 'minOccurs': '0', 'native': False}, 'networks': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'networks', 'minOccurs': '0', 'native': False}, 'floatingIPs': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'floatingips', 'minOccurs': '0', 'native': False}})
        self.networkcredentials = networkcredentials
        self.defaulttenantid = defaulttenantid
        self.routers = routers
        self.hostname = hostname
        self.networkprovidertype = networkprovidertype
        self.networks = networks
        self.floatingips = floatingips 
