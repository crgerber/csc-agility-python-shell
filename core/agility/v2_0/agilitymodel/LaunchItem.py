from core.agility.v2_0.agilitymodel.base.LaunchItem import LaunchItemBase
from core.agility.v2_0.agilitymodel.actions.LaunchItem import LaunchItemActions

class LaunchItem(LaunchItemBase, LaunchItemActions):
    '''
    classdocs
    '''
    def __init__(self, itemId=None, product=None, itemType=None, type='', purchasedBy=None, edition=None, state=None, purchasedOn=None, path=None, prices=list(), accessUriList=None, deployments=list(), itemName=None, resources=list()):
        '''
        Constructor
        @param itemId: itemId
        @type itemId: int
        @param product: product minOccurs=0
        @type product: Link
        @param itemType: itemType minOccurs=0
        @type itemType: string
        @param type: type
        @type type: string
        @param purchasedBy: purchasedBy minOccurs=0
        @type purchasedBy: Link
        @param edition: edition minOccurs=0
        @type edition: Link
        @param state: state minOccurs=0
        @type state: LaunchItemState
        @param purchasedOn: purchasedOn minOccurs=0
        @type purchasedOn: date
        @param path: path minOccurs=0
        @type path: string
        @param prices: prices minOccurs=0 maxOccurs=unbounded
        @type prices: StorePrice
        @param accessUriList: accessUriList minOccurs=0
        @type accessUriList: AccessUriList
        @param deployments: deployments minOccurs=0 maxOccurs=unbounded
        @type deployments: Link
        @param itemName: itemName minOccurs=0
        @type itemName: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        '''
        LaunchItemBase.__init__(self, itemId=itemId, product=product, itemType=itemType, type=type, purchasedBy=purchasedBy, edition=edition, state=state, purchasedOn=purchasedOn, path=path, prices=prices, accessUriList=accessUriList, deployments=deployments, itemName=itemName, resources=resources)
