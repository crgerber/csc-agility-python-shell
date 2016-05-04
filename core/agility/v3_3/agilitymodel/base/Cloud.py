from Item import ItemBase

class CloudBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, enabled=None, variables=[], locations=[], networkservices=[], cloudcredentials=None, priceengine=None, networks=[], postbootscripts=[], prebootscripts=[], cloudlogin=None, hostname=None, networksubscriptions=[], vmmserver=None, cloudadmincredentials=None, models=[], postreleasescripts=[], credentials=[], cloudtype=None, proxies=[], properties=[], subscription=None, cloudcertificate=None, dhcpoptions=[], cloudid=None, repositories=[], vmmport=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'repositories': {'maxOccurs': 'unbounded', 'type': 'Repository', 'name': 'repositories', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'locations': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'locations', 'minOccurs': '0', 'native': False}, 'networkServices': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'networkservices', 'minOccurs': '0', 'native': False}, 'cloudCredentials': {'type': 'Credential', 'name': 'cloudcredentials', 'minOccurs': '0', 'native': False}, 'priceEngine': {'type': 'PriceEngine', 'name': 'priceengine', 'minOccurs': '0', 'native': False}, 'networks': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'networks', 'minOccurs': '0', 'native': False}, 'postBootScripts': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'postbootscripts', 'minOccurs': '0', 'native': False}, 'preBootScripts': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'prebootscripts', 'minOccurs': '0', 'native': False}, 'cloudLogin': {'type': 'Credential', 'name': 'cloudlogin', 'minOccurs': '0', 'native': False}, 'hostname': {'type': 'string', 'name': 'hostname', 'minOccurs': '0', 'native': True}, 'networkSubscriptions': {'maxOccurs': 'unbounded', 'type': 'NetworkSubscription', 'name': 'networksubscriptions', 'minOccurs': '0', 'native': False}, 'vmmServer': {'type': 'string', 'name': 'vmmserver', 'minOccurs': '0', 'native': True}, 'cloudAdminCredentials': {'type': 'Credential', 'name': 'cloudadmincredentials', 'minOccurs': '0', 'native': False}, 'models': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'models', 'minOccurs': '0', 'native': False}, 'postReleaseScripts': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'postreleasescripts', 'minOccurs': '0', 'native': False}, 'credentials': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'credentials', 'minOccurs': '0', 'native': False}, 'cloudType': {'type': 'Link', 'name': 'cloudtype', 'minOccurs': '0', 'native': False}, 'proxies': {'maxOccurs': 'unbounded', 'type': 'Proxy', 'name': 'proxies', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'subscription': {'type': 'string', 'name': 'subscription', 'minOccurs': '0', 'native': True}, 'cloudCertificate': {'type': 'Credential', 'name': 'cloudcertificate', 'minOccurs': '0', 'native': False}, 'dhcpOptions': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'dhcpoptions', 'minOccurs': '0', 'native': False}, 'cloudId': {'type': 'string', 'name': 'cloudid', 'minOccurs': '0', 'native': True}, 'enabled': {'type': 'boolean', 'name': 'enabled', 'minOccurs': '0', 'native': True}, 'vmmPort': {'type': 'int', 'name': 'vmmport', 'minOccurs': '0', 'native': True}})
        self.enabled = enabled
        self.variables = variables
        self.locations = locations
        self.networkservices = networkservices
        self.cloudcredentials = cloudcredentials
        self.priceengine = priceengine
        self.networks = networks
        self.postbootscripts = postbootscripts
        self.prebootscripts = prebootscripts
        self.cloudlogin = cloudlogin
        self.hostname = hostname
        self.networksubscriptions = networksubscriptions
        self.vmmserver = vmmserver
        self.cloudadmincredentials = cloudadmincredentials
        self.models = models
        self.postreleasescripts = postreleasescripts
        self.credentials = credentials
        self.cloudtype = cloudtype
        self.proxies = proxies
        self.properties = properties
        self.subscription = subscription
        self.cloudcertificate = cloudcertificate
        self.dhcpoptions = dhcpoptions
        self.cloudid = cloudid
        self.repositories = repositories
        self.vmmport = vmmport 
