from core.agility.v3_0.agilitymodel.base.CustomItem import CustomItemBase
from core.agility.v3_0.agilitymodel.actions.CustomItem import CustomItemActions

class CustomItem(CustomItemBase, CustomItemActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        CustomItemBase.__init__(self)
