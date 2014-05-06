from core.agility.v3_0.agilitymodel.base.LaunchItem import LaunchItemBase
from core.agility.v3_0.agilitymodel.actions.LaunchItem import LaunchItemActions

class LaunchItem(LaunchItemBase, LaunchItemActions):
    '''
    classdocs
    '''
    def __init__(self, itemid=None, product=None, itemtype=None, type='', purchasedby=None, edition=None, state=None, purchasedon=None, path=None, prices=[], accessurilist=None, deployments=[], itemname=None, resources=[]):
        '''
        Constructor
        @param itemid: itemid
        @type itemid: int
        @param product: product minOccurs=0
        @type product: Link
        @param itemtype: itemtype minOccurs=0
        @type itemtype: string
        @param type: type
        @type type: string
        @param purchasedby: purchasedby minOccurs=0
        @type purchasedby: Link
        @param edition: edition minOccurs=0
        @type edition: Link
        @param state: state minOccurs=0
        @type state: LaunchItemState
        @param purchasedon: purchasedon minOccurs=0
        @type purchasedon: date
        @param path: path minOccurs=0
        @type path: string
        @param prices: prices minOccurs=0 maxOccurs=unbounded
        @type prices: StorePrice
        @param accessurilist: accessurilist minOccurs=0
        @type accessurilist: AccessUriList
        @param deployments: deployments minOccurs=0 maxOccurs=unbounded
        @type deployments: Link
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        '''
        LaunchItemBase.__init__(self, itemid=itemid, product=product, itemtype=itemtype, type=type, purchasedby=purchasedby, edition=edition, state=state, purchasedon=purchasedon, path=path, prices=prices, accessurilist=accessurilist, deployments=deployments, itemname=itemname, resources=resources)
