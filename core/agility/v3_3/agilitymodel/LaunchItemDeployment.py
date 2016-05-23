from core.agility.v3_3.agilitymodel.base.LaunchItemDeployment import LaunchItemDeploymentBase
from core.agility.v3_3.agilitymodel.actions.LaunchItemDeployment import LaunchItemDeploymentActions

class LaunchItemDeployment(LaunchItemDeploymentBase, LaunchItemDeploymentActions):
    '''
    classdocs
    '''
    def __init__(self, launchitem=None, variable=[], deployedby=None, deploymentplan=None, deployedon=None):
        '''
        Constructor
        @param launchitem: launchitem minOccurs=0
        @type launchitem: Link
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        @param deployedby: deployedby minOccurs=0
        @type deployedby: Link
        @param deploymentplan: deploymentplan minOccurs=0
        @type deploymentplan: string
        @param deployedon: deployedon minOccurs=0
        @type deployedon: date
        '''
        LaunchItemDeploymentBase.__init__(self, launchitem=launchitem, variable=variable, deployedby=deployedby, deploymentplan=deploymentplan, deployedon=deployedon)
