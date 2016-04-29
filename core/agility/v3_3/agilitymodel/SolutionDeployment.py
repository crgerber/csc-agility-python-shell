from core.agility.v3_3.agilitymodel.base.SolutionDeployment import SolutionDeploymentBase
from core.agility.v3_3.agilitymodel.actions.SolutionDeployment import SolutionDeploymentActions

class SolutionDeployment(SolutionDeploymentBase, SolutionDeploymentActions):
    '''
    classdocs
    '''
    def __init__(self, solution=None, artifacts=[], artifactversions=[]):
        '''
        Constructor
        @param solution: solution minOccurs=0
        @type solution: Link
        @param artifacts: artifacts minOccurs=0 maxOccurs=unbounded
        @type artifacts: Link
        @param artifactversions: artifactversions minOccurs=0 maxOccurs=unbounded
        @type artifactversions: Artifact
        '''
        SolutionDeploymentBase.__init__(self, solution=solution, artifacts=artifacts, artifactversions=artifactversions)
