from core.agility.v3_3.agilitymodel.base.StoreProductType import StoreProductTypeBase
from core.agility.v3_3.agilitymodel.actions.StoreProductType import StoreProductTypeActions

class StoreProductType(StoreProductTypeBase, StoreProductTypeActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        StoreProductTypeBase.__init__(self)
