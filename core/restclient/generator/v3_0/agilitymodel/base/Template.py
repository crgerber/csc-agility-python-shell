from Item import ItemBase

class TemplateBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, numinstances=None, image=None, instances=[], accesslists=[], cloud=None, configurationresources=[], accessuri=None, factory=None, environment=None, hostnameprefix=None, location=None, variables=[], resources=[], credential=None, srcconnections=[], destconnections=[], packages=[], stack=None, topology=None, releasedisks=None, project=None, volumes=[], model=None, onboarded=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'numInstances': {'type': 'int', 'name': 'numinstances', 'native': True}, 'image': {'type': 'Link', 'name': 'image', 'minOccurs': '0', 'native': False}, 'instances': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'instances', 'minOccurs': '0', 'native': False}, 'accessLists': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'accesslists', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'configurationResources': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'configurationresources', 'minOccurs': '0', 'native': False}, 'accessUri': {'type': 'string', 'name': 'accessuri', 'minOccurs': '0', 'native': True}, 'factory': {'type': 'boolean', 'name': 'factory', 'minOccurs': '0', 'native': True}, 'environment': {'type': 'Link', 'name': 'environment', 'minOccurs': '0', 'native': False}, 'hostnamePrefix': {'type': 'string', 'name': 'hostnameprefix', 'minOccurs': '0', 'native': True}, 'location': {'type': 'string', 'name': 'location', 'minOccurs': '0', 'native': True}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'resources': {'maxOccurs': 'unbounded', 'type': 'Resource', 'name': 'resources', 'minOccurs': '0', 'native': False}, 'credential': {'type': 'Credential', 'name': 'credential', 'minOccurs': '0', 'native': False}, 'srcConnections': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'srcconnections', 'minOccurs': '0', 'native': False}, 'destConnections': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'destconnections', 'minOccurs': '0', 'native': False}, 'packages': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'packages', 'minOccurs': '0', 'native': False}, 'stack': {'type': 'Link', 'name': 'stack', 'minOccurs': '0', 'native': False}, 'topology': {'type': 'Link', 'name': 'topology', 'minOccurs': '0', 'native': False}, 'releaseDisks': {'type': 'boolean', 'name': 'releasedisks', 'minOccurs': '0', 'native': True}, 'project': {'type': 'Link', 'name': 'project', 'minOccurs': '0', 'native': False}, 'volumes': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'volumes', 'minOccurs': '0', 'native': False}, 'model': {'type': 'string', 'name': 'model', 'minOccurs': '0', 'native': True}, 'onboarded': {'type': 'boolean', 'name': 'onboarded', 'minOccurs': '0', 'native': True}})
        self.numinstances = numinstances
        self.image = image
        self.instances = instances
        self.accesslists = accesslists
        self.cloud = cloud
        self.configurationresources = configurationresources
        self.accessuri = accessuri
        self.factory = factory
        self.environment = environment
        self.hostnameprefix = hostnameprefix
        self.location = location
        self.variables = variables
        self.resources = resources
        self.credential = credential
        self.srcconnections = srcconnections
        self.destconnections = destconnections
        self.packages = packages
        self.stack = stack
        self.topology = topology
        self.releasedisks = releasedisks
        self.project = project
        self.volumes = volumes
        self.model = model
        self.onboarded = onboarded 
