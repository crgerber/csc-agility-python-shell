from core.agility.v3_3.agilitymodel.base.LaunchItemDeployment import LaunchItemDeploymentBase
from core.agility.v3_3.agilitymodel.actions.LaunchItemDeployment import LaunchItemDeploymentActions

class LaunchItemDeployment(LaunchItemDeploymentBase, LaunchItemDeploymentActions):
    '''
    classdocs
    '''
    def __init__(self, launchitem=None, deployedon=None, variable=[], deployedby=None, deploymentplan=None):
        '''
        Constructor
        @param launchitem: launchitem minOccurs=0
        @type launchitem: Link
        @param deployedon: deployedon minOccurs=0
        @type deployedon: date
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        @param deployedby: deployedby minOccurs=0
        @type deployedby: Link
        @param deploymentplan: deploymentplan minOccurs=0
        @type deploymentplan: string
        '''
        LaunchItemDeploymentBase.__init__(self, launchitem=launchitem, deployedon=deployedon, variable=variable, deployedby=deployedby, deploymentplan=deploymentplan)
