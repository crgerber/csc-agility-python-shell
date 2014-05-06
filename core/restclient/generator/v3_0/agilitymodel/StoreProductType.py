from base.StoreProductType import StoreProductTypeBase
from actions.StoreProductType import StoreProductTypeActions

class StoreProductType(StoreProductTypeBase, StoreProductTypeActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        StoreProductTypeBase.__init__(self)
