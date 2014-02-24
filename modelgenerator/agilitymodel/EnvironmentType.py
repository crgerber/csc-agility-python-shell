from base.EnvironmentType import EnvironmentTypeBase
from actions.EnvironmentType import EnvironmentTypeActions

class EnvironmentType(EnvironmentTypeBase, EnvironmentTypeActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        EnvironmentTypeBase.__init__(self)
