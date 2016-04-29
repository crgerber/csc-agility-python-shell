from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class TemplateBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, instances=[], numinstances=None, stats=None, credential=None, volumes=[], project=None, accessuri=None, servicebindings=[], cloud=None, packages=[], variables=[], location=None, model=None, destconnections=[], releasedisks=None, configurationresources=[], factory=None, accesslists=[], hostnameprefix=None, srcconnections=[], environment=None, onboarded=None, topology=None, stack=None, image=None, resources=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'instances': {'maxOccurs': 'unbounded', 'native': False, 'name': 'instances', 'minOccurs': '0', 'type': 'Link'}, 'numInstances': {'native': True, 'name': 'numinstances', 'type': 'int'}, 'serviceBindings': {'maxOccurs': 'unbounded', 'native': False, 'name': 'servicebindings', 'minOccurs': '0', 'type': 'Link'}, 'location': {'native': True, 'name': 'location', 'minOccurs': '0', 'type': 'string'}, 'volumes': {'maxOccurs': 'unbounded', 'native': False, 'name': 'volumes', 'minOccurs': '0', 'type': 'Link'}, 'onboarded': {'native': True, 'name': 'onboarded', 'minOccurs': '0', 'type': 'boolean'}, 'configurationResources': {'maxOccurs': 'unbounded', 'native': False, 'name': 'configurationresources', 'minOccurs': '0', 'type': 'Link'}, 'stats': {'native': False, 'name': 'stats', 'minOccurs': '0', 'type': 'TemplateStats'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'packages': {'maxOccurs': 'unbounded', 'native': False, 'name': 'packages', 'minOccurs': '0', 'type': 'Link'}, 'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'AssetProperty'}, 'credential': {'native': False, 'name': 'credential', 'minOccurs': '0', 'type': 'Credential'}, 'model': {'native': True, 'name': 'model', 'minOccurs': '0', 'type': 'string'}, 'destConnections': {'maxOccurs': 'unbounded', 'native': False, 'name': 'destconnections', 'minOccurs': '0', 'type': 'Link'}, 'releaseDisks': {'native': True, 'name': 'releasedisks', 'minOccurs': '0', 'type': 'boolean'}, 'topology': {'native': False, 'name': 'topology', 'minOccurs': '0', 'type': 'Link'}, 'factory': {'native': True, 'name': 'factory', 'minOccurs': '0', 'type': 'boolean'}, 'accessLists': {'maxOccurs': 'unbounded', 'native': False, 'name': 'accesslists', 'minOccurs': '0', 'type': 'Link'}, 'hostnamePrefix': {'native': True, 'name': 'hostnameprefix', 'minOccurs': '0', 'type': 'string'}, 'srcConnections': {'maxOccurs': 'unbounded', 'native': False, 'name': 'srcconnections', 'minOccurs': '0', 'type': 'Link'}, 'environment': {'native': False, 'name': 'environment', 'minOccurs': '0', 'type': 'Link'}, 'project': {'native': False, 'name': 'project', 'minOccurs': '0', 'type': 'Link'}, 'accessUri': {'native': True, 'name': 'accessuri', 'minOccurs': '0', 'type': 'string'}, 'stack': {'native': False, 'name': 'stack', 'minOccurs': '0', 'type': 'Link'}, 'image': {'native': False, 'name': 'image', 'minOccurs': '0', 'type': 'Link'}, 'resources': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resources', 'minOccurs': '0', 'type': 'Resource'}})
        self.instances = instances
        self.numinstances = numinstances
        self.stats = stats
        self.credential = credential
        self.volumes = volumes
        self.project = project
        self.accessuri = accessuri
        self.servicebindings = servicebindings
        self.cloud = cloud
        self.packages = packages
        self.variables = variables
        self.location = location
        self.model = model
        self.destconnections = destconnections
        self.releasedisks = releasedisks
        self.configurationresources = configurationresources
        self.factory = factory
        self.accesslists = accesslists
        self.hostnameprefix = hostnameprefix
        self.srcconnections = srcconnections
        self.environment = environment
        self.onboarded = onboarded
        self.topology = topology
        self.stack = stack
        self.image = image
        self.resources = resources 
