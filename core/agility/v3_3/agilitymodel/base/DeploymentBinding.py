from core.agility.common.AgilityModelBase import AgilityModelBase

class DeploymentBindingBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, artifact=None, id=None, artifacturl=None, platformservice=None, deployer=None, deploymentid=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'artifact': {'name': 'artifact', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'id': {'name': 'id', 'native': True, 'type': 'int'}, 'artifactUrl': {'name': 'artifacturl', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'platformService': {'name': 'platformservice', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'deployer': {'name': 'deployer', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'deploymentId': {'name': 'deploymentid', 'native': True, 'type': 'string'}})
        self.artifact = artifact
        self.id = id
        self.artifacturl = artifacturl
        self.platformservice = platformservice
        self.deployer = deployer
        self.deploymentid = deploymentid 
