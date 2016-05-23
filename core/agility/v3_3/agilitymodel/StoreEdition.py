from core.agility.v3_3.agilitymodel.base.StoreEdition import StoreEditionBase
from core.agility.v3_3.agilitymodel.actions.StoreEdition import StoreEditionActions

class StoreEdition(StoreEditionBase, StoreEditionActions):
    '''
    classdocs
    '''
    def __init__(self, orderassettype=None, itemname=None, version='', release=None, prices=[], resources=[], itemtype=None, itemid=None, deployassettype=None, build=''):
        '''
        Constructor
        @param orderassettype: orderassettype minOccurs=0
        @type orderassettype: Link
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param version: version
        @type version: string
        @param release: release minOccurs=0
        @type release: Link
        @param prices: prices minOccurs=0 maxOccurs=unbounded
        @type prices: StorePrice
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        @param itemtype: itemtype minOccurs=0
        @type itemtype: string
        @param itemid: itemid minOccurs=0
        @type itemid: int
        @param deployassettype: deployassettype minOccurs=0
        @type deployassettype: Link
        @param build: build
        @type build: string
        '''
        StoreEditionBase.__init__(self, orderassettype=orderassettype, itemname=itemname, version=version, release=release, prices=prices, resources=resources, itemtype=itemtype, itemid=itemid, deployassettype=deployassettype, build=build)
