from core.restclient.v2_0.agilitymodel.base.EnvironmentType import EnvironmentTypeBase
from core.restclient.v2_0.agilitymodel.actions.EnvironmentType import EnvironmentTypeActions

class EnvironmentType(EnvironmentTypeBase, EnvironmentTypeActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        EnvironmentTypeBase.__init__(self)
