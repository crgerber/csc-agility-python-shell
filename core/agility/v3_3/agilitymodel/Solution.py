from core.agility.v3_3.agilitymodel.base.Solution import SolutionBase
from core.agility.v3_3.agilitymodel.actions.Solution import SolutionActions

class Solution(SolutionBase, SolutionActions):
    '''
    classdocs
    '''
    def __init__(self, environments=[], variables=[], fixedorder=[], anyorder=[], artifacts=[], deployments=[]):
        '''
        Constructor
        @param environments: environments minOccurs=0 maxOccurs=unbounded
        @type environments: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param fixedorder: fixedorder minOccurs=0 maxOccurs=unbounded
        @type fixedorder: string
        @param anyorder: anyorder minOccurs=0 maxOccurs=unbounded
        @type anyorder: string
        @param artifacts: artifacts minOccurs=0 maxOccurs=unbounded
        @type artifacts: Link
        @param deployments: deployments minOccurs=0 maxOccurs=unbounded
        @type deployments: Link
        '''
        SolutionBase.__init__(self, environments=environments, variables=variables, fixedorder=fixedorder, anyorder=anyorder, artifacts=artifacts, deployments=deployments)
