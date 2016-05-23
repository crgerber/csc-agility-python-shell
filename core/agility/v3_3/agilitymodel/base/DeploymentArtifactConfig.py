from core.agility.common.AgilityModelBase import AgilityModelBase

class DeploymentArtifactConfigBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, variables=[], artifact=None, id=None, services=[], artifacttype=None, properties=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variables': {'name': 'variables', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'artifact': {'name': 'artifact', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'id': {'name': 'id', 'native': True, 'type': 'int'}, 'services': {'name': 'services', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'artifactType': {'name': 'artifacttype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}})
        self.variables = variables
        self.artifact = artifact
        self.id = id
        self.services = services
        self.artifacttype = artifacttype
        self.properties = properties 
