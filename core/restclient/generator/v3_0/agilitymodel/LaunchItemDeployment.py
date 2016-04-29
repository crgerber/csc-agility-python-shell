from .base.LaunchItemDeployment import LaunchItemDeploymentBase
from .actions.LaunchItemDeployment import LaunchItemDeploymentActions

class LaunchItemDeployment(LaunchItemDeploymentBase, LaunchItemDeploymentActions):
    '''
    classdocs
    '''
    def __init__(self, deployedon=None, variable=[], deployedby=None, launchitem=None, deploymentplan=None):
        '''
        Constructor
        @param deployedon: deployedon minOccurs=0
        @type deployedon: date
        @param variable: variable minOccurs=0 maxOccurs=unbounded
        @type variable: AssetProperty
        @param deployedby: deployedby minOccurs=0
        @type deployedby: Link
        @param launchitem: launchitem minOccurs=0
        @type launchitem: Link
        @param deploymentplan: deploymentplan minOccurs=0
        @type deploymentplan: string
        '''
        LaunchItemDeploymentBase.__init__(self, deployedon=deployedon, variable=variable, deployedby=deployedby, launchitem=launchitem, deploymentplan=deploymentplan)
