from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class CloudBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, postreleasescripts=[], hostname=None, postbootscripts=[], vmmserver=None, cloudcredentials=None, cloudcertificate=None, enabled=None, locations=[], credentials=[], networksubscriptions=[], variables=[], priceengine=None, prebootscripts=[], repositories=[], cloudid=None, properties=[], proxies=[], dhcpoptions=[], cloudtype=None, cloudadmincredentials=None, cloudlogin=None, networkservices=[], vmmport=None, subscription=None, networks=[], models=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'networkSubscriptions': {'name': 'networksubscriptions', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'NetworkSubscription'}, 'postBootScripts': {'name': 'postbootscripts', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'vmmServer': {'name': 'vmmserver', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'cloudCredentials': {'name': 'cloudcredentials', 'minOccurs': '0', 'native': False, 'type': 'Credential'}, 'cloudCertificate': {'name': 'cloudcertificate', 'minOccurs': '0', 'native': False, 'type': 'Credential'}, 'enabled': {'name': 'enabled', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'dhcpOptions': {'name': 'dhcpoptions', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'locations': {'name': 'locations', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'credentials': {'name': 'credentials', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'variables': {'name': 'variables', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'priceEngine': {'name': 'priceengine', 'minOccurs': '0', 'native': False, 'type': 'PriceEngine'}, 'cloudId': {'name': 'cloudid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'preBootScripts': {'name': 'prebootscripts', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'repositories': {'name': 'repositories', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Repository'}, 'postReleaseScripts': {'name': 'postreleasescripts', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'proxies': {'name': 'proxies', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Proxy'}, 'hostname': {'name': 'hostname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'cloudType': {'name': 'cloudtype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'cloudAdminCredentials': {'name': 'cloudadmincredentials', 'minOccurs': '0', 'native': False, 'type': 'Credential'}, 'cloudLogin': {'name': 'cloudlogin', 'minOccurs': '0', 'native': False, 'type': 'Credential'}, 'networkServices': {'name': 'networkservices', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'vmmPort': {'name': 'vmmport', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'subscription': {'name': 'subscription', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'networks': {'name': 'networks', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'models': {'name': 'models', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.postreleasescripts = postreleasescripts
        self.hostname = hostname
        self.postbootscripts = postbootscripts
        self.vmmserver = vmmserver
        self.cloudcredentials = cloudcredentials
        self.cloudcertificate = cloudcertificate
        self.enabled = enabled
        self.locations = locations
        self.credentials = credentials
        self.networksubscriptions = networksubscriptions
        self.variables = variables
        self.priceengine = priceengine
        self.prebootscripts = prebootscripts
        self.repositories = repositories
        self.cloudid = cloudid
        self.properties = properties
        self.proxies = proxies
        self.dhcpoptions = dhcpoptions
        self.cloudtype = cloudtype
        self.cloudadmincredentials = cloudadmincredentials
        self.cloudlogin = cloudlogin
        self.networkservices = networkservices
        self.vmmport = vmmport
        self.subscription = subscription
        self.networks = networks
        self.models = models 
