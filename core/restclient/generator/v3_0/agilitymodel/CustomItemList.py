from base.CustomItemList import CustomItemListBase
from actions.CustomItemList import CustomItemListActions

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
