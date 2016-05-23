from core.agility.v3_3.agilitymodel.base.LaunchItem import LaunchItemBase
from core.agility.v3_3.agilitymodel.actions.LaunchItem import LaunchItemActions

class LaunchItem(LaunchItemBase, LaunchItemActions):
    '''
    classdocs
    '''
    def __init__(self, product=None, itemname=None, purchasedby=None, purchasedon=None, state=None, prices=[], edition=None, path=None, accessurilist=None, resources=[], deployments=[], itemid=None, type='', itemtype=None):
        '''
        Constructor
        @param product: product minOccurs=0
        @type product: Link
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param purchasedby: purchasedby minOccurs=0
        @type purchasedby: Link
        @param purchasedon: purchasedon minOccurs=0
        @type purchasedon: date
        @param state: state minOccurs=0
        @type state: LaunchItemState
        @param prices: prices minOccurs=0 maxOccurs=unbounded
        @type prices: StorePrice
        @param edition: edition minOccurs=0
        @type edition: Link
        @param path: path minOccurs=0
        @type path: string
        @param accessurilist: accessurilist minOccurs=0
        @type accessurilist: AccessUriList
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        @param deployments: deployments minOccurs=0 maxOccurs=unbounded
        @type deployments: Link
        @param itemid: itemid
        @type itemid: int
        @param type: type
        @type type: string
        @param itemtype: itemtype minOccurs=0
        @type itemtype: string
        '''
        LaunchItemBase.__init__(self, product=product, itemname=itemname, purchasedby=purchasedby, purchasedon=purchasedon, state=state, prices=prices, edition=edition, path=path, accessurilist=accessurilist, resources=resources, deployments=deployments, itemid=itemid, type=type, itemtype=itemtype)
