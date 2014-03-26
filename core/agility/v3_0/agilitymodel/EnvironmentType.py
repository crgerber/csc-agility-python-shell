from core.agility.v3_0.agilitymodel.base.EnvironmentType import EnvironmentTypeBase
from core.agility.v3_0.agilitymodel.actions.EnvironmentType import EnvironmentTypeActions

class EnvironmentType(EnvironmentTypeBase, EnvironmentTypeActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        EnvironmentTypeBase.__init__(self)
