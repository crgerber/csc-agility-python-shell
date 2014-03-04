from core.restclient.v2_0.agilitymodel.base.DeploymentConfiguration import DeploymentConfigurationBase

class SolutionDeploymentConfigBase(DeploymentConfigurationBase):
    '''
    classdocs
    '''
    def __init__(self, artifactConfigurations=list()):
        DeploymentConfigurationBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'artifactConfigurations': {'maxOccurs': 'unbounded', 'type': 'DeploymentArtifactConfig', 'name': 'artifactConfigurations', 'minOccurs': '0', 'native': False}})
        self.artifactConfigurations = artifactConfigurations 
