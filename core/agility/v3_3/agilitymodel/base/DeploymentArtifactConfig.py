from core.agility.common.AgilityModelBase import AgilityModelBase

class DeploymentArtifactConfigBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, artifact=None, artifacttype=None, properties=[], services=[], id=None, variables=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'artifact': {'native': False, 'name': 'artifact', 'minOccurs': '0', 'type': 'Link'}, 'artifactType': {'native': False, 'name': 'artifacttype', 'minOccurs': '0', 'type': 'Link'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'services': {'maxOccurs': 'unbounded', 'native': True, 'name': 'services', 'minOccurs': '0', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.artifact = artifact
        self.artifacttype = artifacttype
        self.properties = properties
        self.services = services
        self.id = id
        self.variables = variables 
