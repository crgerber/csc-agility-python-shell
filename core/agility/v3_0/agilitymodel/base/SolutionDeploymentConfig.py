from core.agility.v3_0.agilitymodel.base.DeploymentConfiguration import DeploymentConfigurationBase

class SolutionDeploymentConfigBase(DeploymentConfigurationBase):
    '''
    classdocs
    '''
    def __init__(self, artifactconfigurations=[]):
        DeploymentConfigurationBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'artifactConfigurations': {'maxOccurs': 'unbounded', 'type': 'DeploymentArtifactConfig', 'name': 'artifactconfigurations', 'minOccurs': '0', 'native': False}})
        self.artifactconfigurations = artifactconfigurations 
