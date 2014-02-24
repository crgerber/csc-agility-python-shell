from base.SolutionDeploymentConfig import SolutionDeploymentConfigBase
from actions.SolutionDeploymentConfig import SolutionDeploymentConfigActions

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
