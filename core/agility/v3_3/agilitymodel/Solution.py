from core.agility.v3_3.agilitymodel.base.Solution import SolutionBase
from core.agility.v3_3.agilitymodel.actions.Solution import SolutionActions

class Solution(SolutionBase, SolutionActions):
    '''
    classdocs
    '''
    def __init__(self, deployments=[], anyorder=[], environments=[], artifacts=[], fixedorder=[], variables=[]):
        '''
        Constructor
        @param deployments: deployments minOccurs=0 maxOccurs=unbounded
        @type deployments: Link
        @param anyorder: anyorder minOccurs=0 maxOccurs=unbounded
        @type anyorder: string
        @param environments: environments minOccurs=0 maxOccurs=unbounded
        @type environments: Link
        @param artifacts: artifacts minOccurs=0 maxOccurs=unbounded
        @type artifacts: Link
        @param fixedorder: fixedorder minOccurs=0 maxOccurs=unbounded
        @type fixedorder: string
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        '''
        SolutionBase.__init__(self, deployments=deployments, anyorder=anyorder, environments=environments, artifacts=artifacts, fixedorder=fixedorder, variables=variables)
