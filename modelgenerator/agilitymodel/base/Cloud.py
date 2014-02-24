from Item import ItemBase

class CloudBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, enabled=None, variables=list(), locations=list(), networkServices=list(), cloudCredentials=None, priceEngine=None, networks=list(), postBootScripts=list(), preBootScripts=list(), cloudLogin=None, hostname=None, vmmServer=None, postReleaseScripts=list(), credentials=list(), cloudType=None, proxies=list(), properties=list(), subscription=None, cloudCertificate=None, dhcpOptions=list(), cloudId=None, repositories=list(), vmmPort=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'repositories': {'maxOccurs': 'unbounded', 'type': 'Repository', 'name': 'repositories', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'locations': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'locations', 'minOccurs': '0', 'native': False}, 'networkServices': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'networkServices', 'minOccurs': '0', 'native': False}, 'cloudCredentials': {'type': 'Credential', 'name': 'cloudCredentials', 'minOccurs': '0', 'native': False}, 'priceEngine': {'type': 'PriceEngine', 'name': 'priceEngine', 'minOccurs': '0', 'native': False}, 'networks': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'networks', 'minOccurs': '0', 'native': False}, 'postBootScripts': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'postBootScripts', 'minOccurs': '0', 'native': False}, 'preBootScripts': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'preBootScripts', 'minOccurs': '0', 'native': False}, 'cloudLogin': {'type': 'Credential', 'name': 'cloudLogin', 'minOccurs': '0', 'native': False}, 'hostname': {'type': 'string', 'name': 'hostname', 'minOccurs': '0', 'native': True}, 'vmmServer': {'type': 'string', 'name': 'vmmServer', 'minOccurs': '0', 'native': True}, 'postReleaseScripts': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'postReleaseScripts', 'minOccurs': '0', 'native': False}, 'credentials': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'credentials', 'minOccurs': '0', 'native': False}, 'cloudType': {'type': 'Link', 'name': 'cloudType', 'minOccurs': '0', 'native': False}, 'proxies': {'maxOccurs': 'unbounded', 'type': 'Proxy', 'name': 'proxies', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'subscription': {'type': 'string', 'name': 'subscription', 'minOccurs': '0', 'native': True}, 'cloudCertificate': {'type': 'Credential', 'name': 'cloudCertificate', 'minOccurs': '0', 'native': False}, 'dhcpOptions': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'dhcpOptions', 'minOccurs': '0', 'native': False}, 'cloudId': {'type': 'string', 'name': 'cloudId', 'minOccurs': '0', 'native': True}, 'enabled': {'type': 'boolean', 'name': 'enabled', 'minOccurs': '0', 'native': True}, 'vmmPort': {'type': 'int', 'name': 'vmmPort', 'minOccurs': '0', 'native': True}})
        self.enabled = enabled
        self.variables = variables
        self.locations = locations
        self.networkServices = networkServices
        self.cloudCredentials = cloudCredentials
        self.priceEngine = priceEngine
        self.networks = networks
        self.postBootScripts = postBootScripts
        self.preBootScripts = preBootScripts
        self.cloudLogin = cloudLogin
        self.hostname = hostname
        self.vmmServer = vmmServer
        self.postReleaseScripts = postReleaseScripts
        self.credentials = credentials
        self.cloudType = cloudType
        self.proxies = proxies
        self.properties = properties
        self.subscription = subscription
        self.cloudCertificate = cloudCertificate
        self.dhcpOptions = dhcpOptions
        self.cloudId = cloudId
        self.repositories = repositories
        self.vmmPort = vmmPort 
