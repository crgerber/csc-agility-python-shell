from core.agility.v3_3.agilitymodel.base.SolutionDeployment import SolutionDeploymentBase
from core.agility.v3_3.agilitymodel.actions.SolutionDeployment import SolutionDeploymentActions

class SolutionDeployment(SolutionDeploymentBase, SolutionDeploymentActions):
    '''
    classdocs
    '''
    def __init__(self, artifacts=[], artifactversions=[], solution=None):
        '''
        Constructor
        @param artifacts: artifacts minOccurs=0 maxOccurs=unbounded
        @type artifacts: Link
        @param artifactversions: artifactversions minOccurs=0 maxOccurs=unbounded
        @type artifactversions: Artifact
        @param solution: solution minOccurs=0
        @type solution: Link
        '''
        SolutionDeploymentBase.__init__(self, artifacts=artifacts, artifactversions=artifactversions, solution=solution)
