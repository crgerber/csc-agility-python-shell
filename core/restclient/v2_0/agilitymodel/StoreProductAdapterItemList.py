from core.restclient.v2_0.agilitymodel.base.StoreProductAdapterItemList import StoreProductAdapterItemListBase
from core.restclient.v2_0.agilitymodel.actions.StoreProductAdapterItemList import StoreProductAdapterItemListActions

class StoreProductAdapterItemList(StoreProductAdapterItemListBase, StoreProductAdapterItemListActions):
    '''
    classdocs
    '''
    def __init__(self, item=list()):
        '''
        Constructor
        @param item: item minOccurs=0 maxOccurs=unbounded
        @type item: StoreProductAdapterItem
        '''
        StoreProductAdapterItemListBase.__init__(self, item=item)
