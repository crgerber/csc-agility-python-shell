from base.CustomItemList import CustomItemListBase
from actions.CustomItemList import CustomItemListActions

class CustomItemList(CustomItemListBase, CustomItemListActions):
    '''
    classdocs
    '''
    def __init__(self, customItem=list()):
        '''
        Constructor
        @param customItem: customItem minOccurs=0 maxOccurs=unbounded
        @type customItem: CustomItem
        '''
        CustomItemListBase.__init__(self, customItem=customItem)
