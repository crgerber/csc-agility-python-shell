from .base.StoreEditionType import StoreEditionTypeBase
from .actions.StoreEditionType import StoreEditionTypeActions

class StoreEditionType(StoreEditionTypeBase, StoreEditionTypeActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        StoreEditionTypeBase.__init__(self)
