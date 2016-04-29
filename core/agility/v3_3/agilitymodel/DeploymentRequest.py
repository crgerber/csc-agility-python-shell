from core.agility.v3_3.agilitymodel.base.DeploymentRequest import DeploymentRequestBase
from core.agility.v3_3.agilitymodel.actions.DeploymentRequest import DeploymentRequestActions

class DeploymentRequest(DeploymentRequestBase, DeploymentRequestActions):
    '''
    classdocs
    '''
    def __init__(self, checkuse=False, plan=None, variable=[]):
        '''
        Constructor
        @param checkuse: checkuse
        @type checkuse: boolean
        @param plan: plan
        @type plan: DeploymentPlan
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        '''
        DeploymentRequestBase.__init__(self, checkuse=checkuse, plan=plan, variable=variable)
