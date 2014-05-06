from AgilityModelBase import AgilityModelBase

class DeploymentBindingBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, deployer=None, deploymentid='', artifact=None, artifacturl=None, platformservice=None, id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'deployer': {'type': 'Link', 'name': 'deployer', 'minOccurs': '0', 'native': False}, 'artifactUrl': {'type': 'string', 'name': 'artifacturl', 'minOccurs': '0', 'native': True}, 'artifact': {'type': 'Link', 'name': 'artifact', 'minOccurs': '0', 'native': False}, 'deploymentId': {'type': 'string', 'name': 'deploymentid', 'native': True}, 'platformService': {'type': 'Link', 'name': 'platformservice', 'minOccurs': '0', 'native': False}, 'id': {'type': 'int', 'name': 'id', 'native': True}})
        self.deployer = deployer
        self.deploymentid = deploymentid
        self.artifact = artifact
        self.artifacturl = artifacturl
        self.platformservice = platformservice
        self.id = id 
