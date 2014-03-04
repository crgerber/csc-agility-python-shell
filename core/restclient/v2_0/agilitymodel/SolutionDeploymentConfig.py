from core.restclient.v2_0.agilitymodel.base.SolutionDeploymentConfig import SolutionDeploymentConfigBase
from core.restclient.v2_0.agilitymodel.actions.SolutionDeploymentConfig import SolutionDeploymentConfigActions

class SolutionDeploymentConfig(SolutionDeploymentConfigBase, SolutionDeploymentConfigActions):
    '''
    classdocs
    '''
    def __init__(self, artifactConfigurations=list()):
        '''
        Constructor
        @param artifactConfigurations: artifactConfigurations minOccurs=0 maxOccurs=unbounded
        @type artifactConfigurations: DeploymentArtifactConfig
        '''
        SolutionDeploymentConfigBase.__init__(self, artifactConfigurations=artifactConfigurations)
