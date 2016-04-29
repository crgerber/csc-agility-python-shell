from .base.Solution import SolutionBase
from .actions.Solution import SolutionActions

class Solution(SolutionBase, SolutionActions):
    '''
    classdocs
    '''
    def __init__(self, artifacts=[], variables=[], environments=[], deployments=[], fixedorder=[], anyorder=[]):
        '''
        Constructor
        @param artifacts: artifacts minOccurs=0 maxOccurs=unbounded
        @type artifacts: Link
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: AssetProperty
        @param environments: environments minOccurs=0 maxOccurs=unbounded
        @type environments: Link
        @param deployments: deployments minOccurs=0 maxOccurs=unbounded
        @type deployments: Link
        @param fixedorder: fixedorder minOccurs=0 maxOccurs=unbounded
        @type fixedorder: string
        @param anyorder: anyorder minOccurs=0 maxOccurs=unbounded
        @type anyorder: string
        '''
        SolutionBase.__init__(self, artifacts=artifacts, variables=variables, environments=environments, deployments=deployments, fixedorder=fixedorder, anyorder=anyorder)
