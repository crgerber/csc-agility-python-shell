from core.restclient.v2_0.agilitymodel.base.DeploymentRequest import DeploymentRequestBase
from core.restclient.v2_0.agilitymodel.actions.DeploymentRequest import DeploymentRequestActions

class DeploymentRequest(DeploymentRequestBase, DeploymentRequestActions):
    '''
    classdocs
    '''
    def __init__(self, variable=list(), checkUse=False, plan=None):
        '''
        Constructor
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        @param checkUse: checkUse
        @type checkUse: boolean
        @param plan: plan
        @type plan: DeploymentPlan
        '''
        DeploymentRequestBase.__init__(self, variable=variable, checkUse=checkUse, plan=plan)
