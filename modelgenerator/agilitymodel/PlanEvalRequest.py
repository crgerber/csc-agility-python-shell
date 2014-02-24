from base.PlanEvalRequest import PlanEvalRequestBase
from actions.PlanEvalRequest import PlanEvalRequestActions

class PlanEvalRequest(PlanEvalRequestBase, PlanEvalRequestActions):
    '''
    classdocs
    '''
    def __init__(self, logLevel=None, additionalPolicyId=list()):
        '''
        Constructor
        @param logLevel: logLevel minOccurs=0
        @type logLevel: int
        @param additionalPolicyId: additionalPolicyId minOccurs=0 maxOccurs=unbounded
        @type additionalPolicyId: int
        '''
        PlanEvalRequestBase.__init__(self, logLevel=logLevel, additionalPolicyId=additionalPolicyId)
