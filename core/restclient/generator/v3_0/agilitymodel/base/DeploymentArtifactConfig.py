from .AgilityModelBase import AgilityModelBase

class DeploymentArtifactConfigBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, variables=[], artifact=None, properties=[], services=[], artifacttype=None, id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'artifact': {'type': 'Link', 'name': 'artifact', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'services': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'services', 'minOccurs': '0', 'native': True}, 'artifactType': {'type': 'Link', 'name': 'artifacttype', 'minOccurs': '0', 'native': False}, 'id': {'type': 'int', 'name': 'id', 'native': True}})
        self.variables = variables
        self.artifact = artifact
        self.properties = properties
        self.services = services
        self.artifacttype = artifacttype
        self.id = id 
