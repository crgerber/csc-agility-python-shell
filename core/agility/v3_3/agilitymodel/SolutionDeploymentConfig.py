from base.SolutionDeploymentConfig import SolutionDeploymentConfigBase
from actions.SolutionDeploymentConfig import SolutionDeploymentConfigActions

class SolutionDeploymentConfig(SolutionDeploymentConfigBase, SolutionDeploymentConfigActions):
    '''
    classdocs
    '''
    def __init__(self, artifactconfigurations=[]):
        '''
        Constructor
        @param artifactconfigurations: artifactconfigurations minOccurs=0 maxOccurs=unbounded
        @type artifactconfigurations: DeploymentArtifactConfig
        '''
        SolutionDeploymentConfigBase.__init__(self, artifactconfigurations=artifactconfigurations)
