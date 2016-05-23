from core.agility.v3_3.agilitymodel.base.DeploymentRequest import DeploymentRequestBase
from core.agility.v3_3.agilitymodel.actions.DeploymentRequest import DeploymentRequestActions

class DeploymentRequest(DeploymentRequestBase, DeploymentRequestActions):
    '''
    classdocs
    '''
    def __init__(self, plan=None, variable=[], checkuse=False):
        '''
        Constructor
        @param plan: plan
        @type plan: DeploymentPlan
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        @param checkuse: checkuse
        @type checkuse: boolean
        '''
        DeploymentRequestBase.__init__(self, plan=plan, variable=variable, checkuse=checkuse)
