from .base.DeploymentConfiguration import DeploymentConfigurationBase
from .actions.DeploymentConfiguration import DeploymentConfigurationActions

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
