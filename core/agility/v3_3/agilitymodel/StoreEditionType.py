from core.agility.v3_3.agilitymodel.base.StoreEditionType import StoreEditionTypeBase
from core.agility.v3_3.agilitymodel.actions.StoreEditionType import StoreEditionTypeActions

class StoreEditionType(StoreEditionTypeBase, StoreEditionTypeActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        StoreEditionTypeBase.__init__(self)
