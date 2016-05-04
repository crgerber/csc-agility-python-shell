from core.agility.v3_3.agilitymodel.base.DeploymentConfiguration import DeploymentConfigurationBase
from core.agility.v3_3.agilitymodel.actions.DeploymentConfiguration import DeploymentConfigurationActions

class DeploymentConfiguration(DeploymentConfigurationBase, DeploymentConfigurationActions):
    '''
    classdocs
    '''
    def __init__(self, id=None):
        '''
        Constructor
        @param id: id
        @type id: int
        '''
        DeploymentConfigurationBase.__init__(self, id=id)
