from core.restclient.v2_0.agilitymodel.base.DeploymentConfiguration import DeploymentConfigurationBase
from core.restclient.v2_0.agilitymodel.actions.DeploymentConfiguration import DeploymentConfigurationActions

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
