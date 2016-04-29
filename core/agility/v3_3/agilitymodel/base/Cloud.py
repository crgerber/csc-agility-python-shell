from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class CloudBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, credentials=[], networks=[], dhcpoptions=[], postbootscripts=[], networkservices=[], networksubscriptions=[], postreleasescripts=[], prebootscripts=[], cloudlogin=None, vmmserver=None, hostname=None, vmmport=None, cloudcertificate=None, cloudcredentials=None, properties=[], cloudtype=None, cloudadmincredentials=None, locations=[], repositories=[], priceengine=None, subscription=None, cloudid=None, proxies=[], enabled=None, variables=[], models=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credentials': {'maxOccurs': 'unbounded', 'native': False, 'name': 'credentials', 'minOccurs': '0', 'type': 'Link'}, 'vmmServer': {'native': True, 'name': 'vmmserver', 'minOccurs': '0', 'type': 'string'}, 'dhcpOptions': {'maxOccurs': 'unbounded', 'native': False, 'name': 'dhcpoptions', 'minOccurs': '0', 'type': 'Link'}, 'postBootScripts': {'maxOccurs': 'unbounded', 'native': False, 'name': 'postbootscripts', 'minOccurs': '0', 'type': 'Link'}, 'cloudAdminCredentials': {'native': False, 'name': 'cloudadmincredentials', 'minOccurs': '0', 'type': 'Credential'}, 'postReleaseScripts': {'maxOccurs': 'unbounded', 'native': False, 'name': 'postreleasescripts', 'minOccurs': '0', 'type': 'Link'}, 'preBootScripts': {'maxOccurs': 'unbounded', 'native': False, 'name': 'prebootscripts', 'minOccurs': '0', 'type': 'Link'}, 'cloudLogin': {'native': False, 'name': 'cloudlogin', 'minOccurs': '0', 'type': 'Credential'}, 'hostname': {'native': True, 'name': 'hostname', 'minOccurs': '0', 'type': 'string'}, 'vmmPort': {'native': True, 'name': 'vmmport', 'minOccurs': '0', 'type': 'int'}, 'proxies': {'maxOccurs': 'unbounded', 'native': False, 'name': 'proxies', 'minOccurs': '0', 'type': 'Proxy'}, 'cloudCertificate': {'native': False, 'name': 'cloudcertificate', 'minOccurs': '0', 'type': 'Credential'}, 'cloudCredentials': {'native': False, 'name': 'cloudcredentials', 'minOccurs': '0', 'type': 'Credential'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'cloudType': {'native': False, 'name': 'cloudtype', 'minOccurs': '0', 'type': 'Link'}, 'models': {'maxOccurs': 'unbounded', 'native': False, 'name': 'models', 'minOccurs': '0', 'type': 'Link'}, 'networkServices': {'maxOccurs': 'unbounded', 'native': False, 'name': 'networkservices', 'minOccurs': '0', 'type': 'Link'}, 'locations': {'maxOccurs': 'unbounded', 'native': False, 'name': 'locations', 'minOccurs': '0', 'type': 'Link'}, 'repositories': {'maxOccurs': 'unbounded', 'native': False, 'name': 'repositories', 'minOccurs': '0', 'type': 'Repository'}, 'priceEngine': {'native': False, 'name': 'priceengine', 'minOccurs': '0', 'type': 'PriceEngine'}, 'subscription': {'native': True, 'name': 'subscription', 'minOccurs': '0', 'type': 'string'}, 'cloudId': {'native': True, 'name': 'cloudid', 'minOccurs': '0', 'type': 'string'}, 'networks': {'maxOccurs': 'unbounded', 'native': False, 'name': 'networks', 'minOccurs': '0', 'type': 'Link'}, 'enabled': {'native': True, 'name': 'enabled', 'minOccurs': '0', 'type': 'boolean'}, 'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'AssetProperty'}, 'networkSubscriptions': {'maxOccurs': 'unbounded', 'native': False, 'name': 'networksubscriptions', 'minOccurs': '0', 'type': 'NetworkSubscription'}})
        self.credentials = credentials
        self.networks = networks
        self.dhcpoptions = dhcpoptions
        self.postbootscripts = postbootscripts
        self.networkservices = networkservices
        self.networksubscriptions = networksubscriptions
        self.postreleasescripts = postreleasescripts
        self.prebootscripts = prebootscripts
        self.cloudlogin = cloudlogin
        self.vmmserver = vmmserver
        self.hostname = hostname
        self.vmmport = vmmport
        self.cloudcertificate = cloudcertificate
        self.cloudcredentials = cloudcredentials
        self.properties = properties
        self.cloudtype = cloudtype
        self.cloudadmincredentials = cloudadmincredentials
        self.locations = locations
        self.repositories = repositories
        self.priceengine = priceengine
        self.subscription = subscription
        self.cloudid = cloudid
        self.proxies = proxies
        self.enabled = enabled
        self.variables = variables
        self.models = models 
