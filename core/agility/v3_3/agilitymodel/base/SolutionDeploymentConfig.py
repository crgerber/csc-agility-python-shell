from core.agility.v3_3.agilitymodel.base.DeploymentConfiguration import DeploymentConfigurationBase

class SolutionDeploymentConfigBase(DeploymentConfigurationBase):
    '''
    classdocs
    '''
    def __init__(self, artifactconfigurations=[]):
        DeploymentConfigurationBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'artifactConfigurations': {'maxOccurs': 'unbounded', 'native': False, 'name': 'artifactconfigurations', 'minOccurs': '0', 'type': 'DeploymentArtifactConfig'}})
        self.artifactconfigurations = artifactconfigurations 
