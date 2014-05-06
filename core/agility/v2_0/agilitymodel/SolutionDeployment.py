from core.agility.v2_0.agilitymodel.base.SolutionDeployment import SolutionDeploymentBase
from core.agility.v2_0.agilitymodel.actions.SolutionDeployment import SolutionDeploymentActions

class SolutionDeployment(SolutionDeploymentBase, SolutionDeploymentActions):
    '''
    classdocs
    '''
    def __init__(self, artifacts=list(), solution=None, artifactVersions=list()):
        '''
        Constructor
        @param artifacts: artifacts minOccurs=0 maxOccurs=unbounded
        @type artifacts: Link
        @param solution: solution minOccurs=0
        @type solution: Link
        @param artifactVersions: artifactVersions minOccurs=0 maxOccurs=unbounded
        @type artifactVersions: Artifact
        '''
        SolutionDeploymentBase.__init__(self, artifacts=artifacts, solution=solution, artifactVersions=artifactVersions)
