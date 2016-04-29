from core.agility.v3_3.agilitymodel.base.CustomItemList import CustomItemListBase
from core.agility.v3_3.agilitymodel.actions.CustomItemList import CustomItemListActions

class CustomItemList(CustomItemListBase, CustomItemListActions):
    '''
    classdocs
    '''
    def __init__(self, customitem=[]):
        '''
        Constructor
        @param customitem: customitem minOccurs=0 maxOccurs=unbounded
        @type customitem: CustomItem
        '''
        CustomItemListBase.__init__(self, customitem=customitem)
