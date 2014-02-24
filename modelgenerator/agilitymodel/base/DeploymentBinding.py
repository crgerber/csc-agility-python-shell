from AgilityModelBase import AgilityModelBase

class DeploymentBindingBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, deployer=None, deploymentId='', artifact=None, artifactUrl=None, platformService=None, id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'deployer': {'type': 'Link', 'name': 'deployer', 'minOccurs': '0', 'native': False}, 'artifactUrl': {'type': 'string', 'name': 'artifactUrl', 'minOccurs': '0', 'native': True}, 'artifact': {'type': 'Link', 'name': 'artifact', 'minOccurs': '0', 'native': False}, 'deploymentId': {'type': 'string', 'name': 'deploymentId', 'native': True}, 'platformService': {'type': 'Link', 'name': 'platformService', 'minOccurs': '0', 'native': False}, 'id': {'type': 'int', 'name': 'id', 'native': True}})
        self.deployer = deployer
        self.deploymentId = deploymentId
        self.artifact = artifact
        self.artifactUrl = artifactUrl
        self.platformService = platformService
        self.id = id 
