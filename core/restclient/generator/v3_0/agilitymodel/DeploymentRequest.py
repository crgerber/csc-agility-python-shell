from .base.DeploymentRequest import DeploymentRequestBase
from .actions.DeploymentRequest import DeploymentRequestActions

class DeploymentRequest(DeploymentRequestBase, DeploymentRequestActions):
    '''
    classdocs
    '''
    def __init__(self, variable=[], checkuse=False, plan=None):
        '''
        Constructor
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        @param checkuse: checkuse
        @type checkuse: boolean
        @param plan: plan
        @type plan: DeploymentPlan
        '''
        DeploymentRequestBase.__init__(self, variable=variable, checkuse=checkuse, plan=plan)
