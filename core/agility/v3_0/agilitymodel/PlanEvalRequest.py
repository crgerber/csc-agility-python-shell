from core.agility.v3_0.agilitymodel.base.PlanEvalRequest import PlanEvalRequestBase
from core.agility.v3_0.agilitymodel.actions.PlanEvalRequest import PlanEvalRequestActions

class PlanEvalRequest(PlanEvalRequestBase, PlanEvalRequestActions):
    '''
    classdocs
    '''
    def __init__(self, loglevel=None, additionalpolicyid=[], ignorerequiredproperties=False):
        '''
        Constructor
        @param loglevel: loglevel minOccurs=0
        @type loglevel: int
        @param additionalpolicyid: additionalpolicyid minOccurs=0 maxOccurs=unbounded
        @type additionalpolicyid: int
        @param ignorerequiredproperties: ignorerequiredproperties
        @type ignorerequiredproperties: boolean
        '''
        PlanEvalRequestBase.__init__(self, loglevel=loglevel, additionalpolicyid=additionalpolicyid, ignorerequiredproperties=ignorerequiredproperties)
