from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class TemplateBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, credential=None, onboarded=None, numInstances=None, volumes=list(), hostnamePrefix=None, image=None, resources=list(), factory=None, srcConnections=list(), instances=list(), accessUri=None, location=None, accessLists=list(), destConnections=list(), variables=list(), model=None, packages=list(), configurationResources=list(), stack=None, cloud=None, topology=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'credential': {'type': 'Credential', 'name': 'credential', 'minOccurs': '0', 'native': False}, 'packages': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'packages', 'minOccurs': '0', 'native': False}, 'numInstances': {'type': 'int', 'name': 'numInstances', 'native': True}, 'accessUri': {'type': 'string', 'name': 'accessUri', 'minOccurs': '0', 'native': True}, 'instances': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'instances', 'minOccurs': '0', 'native': False}, 'stack': {'type': 'Link', 'name': 'stack', 'minOccurs': '0', 'native': False}, 'image': {'type': 'Link', 'name': 'image', 'minOccurs': '0', 'native': False}, 'factory': {'type': 'boolean', 'name': 'factory', 'minOccurs': '0', 'native': True}, 'topology': {'type': 'Link', 'name': 'topology', 'minOccurs': '0', 'native': False}, 'srcConnections': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'srcConnections', 'minOccurs': '0', 'native': False}, 'hostnamePrefix': {'type': 'string', 'name': 'hostnamePrefix', 'minOccurs': '0', 'native': True}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'location': {'type': 'string', 'name': 'location', 'minOccurs': '0', 'native': True}, 'volumes': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'volumes', 'minOccurs': '0', 'native': False}, 'destConnections': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'destConnections', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'model': {'type': 'string', 'name': 'model', 'minOccurs': '0', 'native': True}, 'onboarded': {'type': 'boolean', 'name': 'onboarded', 'minOccurs': '0', 'native': True}, 'accessLists': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'accessLists', 'minOccurs': '0', 'native': False}, 'resources': {'maxOccurs': 'unbounded', 'type': 'Resource', 'name': 'resources', 'minOccurs': '0', 'native': False}, 'configurationResources': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'configurationResources', 'minOccurs': '0', 'native': False}})
        self.credential = credential
        self.onboarded = onboarded
        self.numInstances = numInstances
        self.volumes = volumes
        self.hostnamePrefix = hostnamePrefix
        self.image = image
        self.resources = resources
        self.factory = factory
        self.srcConnections = srcConnections
        self.instances = instances
        self.accessUri = accessUri
        self.location = location
        self.accessLists = accessLists
        self.destConnections = destConnections
        self.variables = variables
        self.model = model
        self.packages = packages
        self.configurationResources = configurationResources
        self.stack = stack
        self.cloud = cloud
        self.topology = topology 
