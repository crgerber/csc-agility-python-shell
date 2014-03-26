from core.agility.v3_0.agilitymodel.base.StoreReleaseType import StoreReleaseTypeBase
from core.agility.v3_0.agilitymodel.actions.StoreReleaseType import StoreReleaseTypeActions

class StoreReleaseType(StoreReleaseTypeBase, StoreReleaseTypeActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        StoreReleaseTypeBase.__init__(self)
