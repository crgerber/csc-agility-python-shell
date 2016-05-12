from core.agility.v3_3.agilitymodel.base.StoreProductAdapterItemList import StoreProductAdapterItemListBase
from core.agility.v3_3.agilitymodel.actions.StoreProductAdapterItemList import StoreProductAdapterItemListActions

class StoreProductAdapterItemList(StoreProductAdapterItemListBase, StoreProductAdapterItemListActions):
    '''
    classdocs
    '''
    def __init__(self, item=[]):
        '''
        Constructor
        @param item: item minOccurs=0 maxOccurs=unbounded
        @type item: StoreProductAdapterItem
        '''
        StoreProductAdapterItemListBase.__init__(self, item=item)