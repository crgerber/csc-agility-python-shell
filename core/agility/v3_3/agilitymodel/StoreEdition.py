from core.agility.v3_3.agilitymodel.base.StoreEdition import StoreEditionBase
from core.agility.v3_3.agilitymodel.actions.StoreEdition import StoreEditionActions

class StoreEdition(StoreEditionBase, StoreEditionActions):
    '''
    classdocs
    '''
    def __init__(self, itemtype=None, deployassettype=None, release=None, prices=[], build='', itemid=None, version='', resources=[], itemname=None, orderassettype=None):
        '''
        Constructor
        @param itemtype: itemtype minOccurs=0
        @type itemtype: string
        @param deployassettype: deployassettype minOccurs=0
        @type deployassettype: Link
        @param release: release minOccurs=0
        @type release: Link
        @param prices: prices minOccurs=0 maxOccurs=unbounded
        @type prices: StorePrice
        @param build: build
        @type build: string
        @param itemid: itemid minOccurs=0
        @type itemid: int
        @param version: version
        @type version: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param orderassettype: orderassettype minOccurs=0
        @type orderassettype: Link
        '''
        StoreEditionBase.__init__(self, itemtype=itemtype, deployassettype=deployassettype, release=release, prices=prices, build=build, itemid=itemid, version=version, resources=resources, itemname=itemname, orderassettype=orderassettype)
