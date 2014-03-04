from core.restclient.v2_0.agilitymodel.base.LaunchItemDeployment import LaunchItemDeploymentBase
from core.restclient.v2_0.agilitymodel.actions.LaunchItemDeployment import LaunchItemDeploymentActions

class LaunchItemDeployment(LaunchItemDeploymentBase, LaunchItemDeploymentActions):
    '''
    classdocs
    '''
    def __init__(self, deployedOn=None, variable=list(), deployedBy=None, launchItem=None, deploymentPlan=None):
        '''
        Constructor
        @param deployedOn: deployedOn minOccurs=0
        @type deployedOn: date
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        @param deployedBy: deployedBy minOccurs=0
        @type deployedBy: Link
        @param launchItem: launchItem minOccurs=0
        @type launchItem: Link
        @param deploymentPlan: deploymentPlan minOccurs=0
        @type deploymentPlan: string
        '''
        LaunchItemDeploymentBase.__init__(self, deployedOn=deployedOn, variable=variable, deployedBy=deployedBy, launchItem=launchItem, deploymentPlan=deploymentPlan)
