from .base.StoreCategory import StoreCategoryBase
from .actions.StoreCategory import StoreCategoryActions

class StoreCategory(StoreCategoryBase, StoreCategoryActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        StoreCategoryBase.__init__(self)
