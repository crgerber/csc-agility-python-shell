from core.agility.v3_3.agilitymodel.base.StoreCategory import StoreCategoryBase
from core.agility.v3_3.agilitymodel.actions.StoreCategory import StoreCategoryActions

class StoreCategory(StoreCategoryBase, StoreCategoryActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        StoreCategoryBase.__init__(self)
