from core.agility.v3_3.agilitymodel.base.PlanEvalRequest import PlanEvalRequestBase
from core.agility.v3_3.agilitymodel.actions.PlanEvalRequest import PlanEvalRequestActions

class PlanEvalRequest(PlanEvalRequestBase, PlanEvalRequestActions):
    '''
    classdocs
    '''
    def __init__(self, loglevel=None, additionalpolicyid=[], ignorerequiredproperties=False, templateid=None):
        '''
        Constructor
        @param loglevel: loglevel minOccurs=0
        @type loglevel: int
        @param additionalpolicyid: additionalpolicyid minOccurs=0 maxOccurs=unbounded
        @type additionalpolicyid: int
        @param ignorerequiredproperties: ignorerequiredproperties
        @type ignorerequiredproperties: boolean
        @param templateid: templateid minOccurs=0
        @type templateid: int
        '''
        PlanEvalRequestBase.__init__(self, loglevel=loglevel, additionalpolicyid=additionalpolicyid, ignorerequiredproperties=ignorerequiredproperties, templateid=templateid)
