from core.agility.v3_3.agilitymodel.base.LaunchItem import LaunchItemBase
from core.agility.v3_3.agilitymodel.actions.LaunchItem import LaunchItemActions

class LaunchItem(LaunchItemBase, LaunchItemActions):
    '''
    classdocs
    '''
    def __init__(self, edition=None, path=None, resources=[], itemid=None, state=None, type='', itemtype=None, deployments=[], accessurilist=None, purchasedon=None, itemname=None, prices=[], purchasedby=None, product=None):
        '''
        Constructor
        @param edition: edition minOccurs=0
        @type edition: Link
        @param path: path minOccurs=0
        @type path: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        @param itemid: itemid
        @type itemid: int
        @param state: state minOccurs=0
        @type state: LaunchItemState
        @param type: type
        @type type: string
        @param itemtype: itemtype minOccurs=0
        @type itemtype: string
        @param deployments: deployments minOccurs=0 maxOccurs=unbounded
        @type deployments: Link
        @param accessurilist: accessurilist minOccurs=0
        @type accessurilist: AccessUriList
        @param purchasedon: purchasedon minOccurs=0
        @type purchasedon: date
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param prices: prices minOccurs=0 maxOccurs=unbounded
        @type prices: StorePrice
        @param purchasedby: purchasedby minOccurs=0
        @type purchasedby: Link
        @param product: product minOccurs=0
        @type product: Link
        '''
        LaunchItemBase.__init__(self, edition=edition, path=path, resources=resources, itemid=itemid, state=state, type=type, itemtype=itemtype, deployments=deployments, accessurilist=accessurilist, purchasedon=purchasedon, itemname=itemname, prices=prices, purchasedby=purchasedby, product=product)
