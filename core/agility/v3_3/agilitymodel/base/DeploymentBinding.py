from core.agility.common.AgilityModelBase import AgilityModelBase

class DeploymentBindingBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, platformservice=None, deployer=None, artifact=None, artifacturl=None, deploymentid='', id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'platformService': {'native': False, 'name': 'platformservice', 'minOccurs': '0', 'type': 'Link'}, 'deployer': {'native': False, 'name': 'deployer', 'minOccurs': '0', 'type': 'Link'}, 'artifact': {'native': False, 'name': 'artifact', 'minOccurs': '0', 'type': 'Link'}, 'artifactUrl': {'native': True, 'name': 'artifacturl', 'minOccurs': '0', 'type': 'string'}, 'deploymentId': {'native': True, 'name': 'deploymentid', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}})
        self.platformservice = platformservice
        self.deployer = deployer
        self.artifact = artifact
        self.artifacturl = artifacturl
        self.deploymentid = deploymentid
        self.id = id 
