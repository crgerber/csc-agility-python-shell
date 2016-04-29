from .base.StoreReleaseType import StoreReleaseTypeBase
from .actions.StoreReleaseType import StoreReleaseTypeActions

class StoreReleaseType(StoreReleaseTypeBase, StoreReleaseTypeActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        StoreReleaseTypeBase.__init__(self)
