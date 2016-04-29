from .base.CustomItem import CustomItemBase
from .actions.CustomItem import CustomItemActions

class CustomItem(CustomItemBase, CustomItemActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        CustomItemBase.__init__(self)
