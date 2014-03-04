from core.restclient.v2_0.agilitymodel.base.StoreEditionType import StoreEditionTypeBase
from core.restclient.v2_0.agilitymodel.actions.StoreEditionType import StoreEditionTypeActions

class StoreEditionType(StoreEditionTypeBase, StoreEditionTypeActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        StoreEditionTypeBase.__init__(self)
