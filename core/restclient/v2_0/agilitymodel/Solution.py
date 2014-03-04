from core.restclient.v2_0.agilitymodel.base.Solution import SolutionBase
from core.restclient.v2_0.agilitymodel.actions.Solution import SolutionActions

class Solution(SolutionBase, SolutionActions):
    '''
    classdocs
    '''
    def __init__(self, artifacts=list(), variables=list(), environments=list(), deployments=list(), fixedOrder=list(), anyOrder=list()):
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
        @param fixedOrder: fixedOrder minOccurs=0 maxOccurs=unbounded
        @type fixedOrder: string
        @param anyOrder: anyOrder minOccurs=0 maxOccurs=unbounded
        @type anyOrder: string
        '''
        SolutionBase.__init__(self, artifacts=artifacts, variables=variables, environments=environments, deployments=deployments, fixedOrder=fixedOrder, anyOrder=anyOrder)
