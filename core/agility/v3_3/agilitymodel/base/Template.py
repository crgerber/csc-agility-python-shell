from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class TemplateBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, topology=None, accessuri=None, hostnameprefix=None, onboarded=None, location=None, configurationresources=[], destconnections=[], model=None, accesslists=[], releasedisks=None, factory=None, cloud=None, variables=[], resources=[], numinstances=None, credential=None, environment=None, servicebindings=[], srcconnections=[], packages=[], stack=None, project=None, instances=[], stats=None, volumes=[], image=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'topology': {'name': 'topology', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'accessUri': {'name': 'accessuri', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'hostnamePrefix': {'name': 'hostnameprefix', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'onboarded': {'name': 'onboarded', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'location': {'name': 'location', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'configurationResources': {'name': 'configurationresources', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'destConnections': {'name': 'destconnections', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'model': {'name': 'model', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'accessLists': {'name': 'accesslists', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'releaseDisks': {'name': 'releasedisks', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'factory': {'name': 'factory', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'variables': {'name': 'variables', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'resources': {'name': 'resources', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Resource'}, 'numInstances': {'name': 'numinstances', 'native': True, 'type': 'int'}, 'credential': {'name': 'credential', 'minOccurs': '0', 'native': False, 'type': 'Credential'}, 'environment': {'name': 'environment', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'serviceBindings': {'name': 'servicebindings', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'srcConnections': {'name': 'srcconnections', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'packages': {'name': 'packages', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'stack': {'name': 'stack', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'project': {'name': 'project', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'instances': {'name': 'instances', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'stats': {'name': 'stats', 'minOccurs': '0', 'native': False, 'type': 'TemplateStats'}, 'volumes': {'name': 'volumes', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'image': {'name': 'image', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.topology = topology
        self.accessuri = accessuri
        self.hostnameprefix = hostnameprefix
        self.onboarded = onboarded
        self.location = location
        self.configurationresources = configurationresources
        self.destconnections = destconnections
        self.model = model
        self.accesslists = accesslists
        self.releasedisks = releasedisks
        self.factory = factory
        self.cloud = cloud
        self.variables = variables
        self.resources = resources
        self.numinstances = numinstances
        self.credential = credential
        self.environment = environment
        self.servicebindings = servicebindings
        self.srcconnections = srcconnections
        self.packages = packages
        self.stack = stack
        self.project = project
        self.instances = instances
        self.stats = stats
        self.volumes = volumes
        self.image = image 
