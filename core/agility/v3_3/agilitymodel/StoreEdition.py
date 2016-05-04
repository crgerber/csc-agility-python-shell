from base.StoreEdition import StoreEditionBase
from actions.StoreEdition import StoreEditionActions

class StoreEdition(StoreEditionBase, StoreEditionActions):
    '''
    classdocs
    '''
    def __init__(self, itemid=None, deployassettype=None, itemtype=None, orderassettype=None, prices=[], version='', build='', release=None, itemname=None, resources=[]):
        '''
        Constructor
        @param itemid: itemid minOccurs=0
        @type itemid: int
        @param deployassettype: deployassettype minOccurs=0
        @type deployassettype: Link
        @param itemtype: itemtype minOccurs=0
        @type itemtype: string
        @param orderassettype: orderassettype minOccurs=0
        @type orderassettype: Link
        @param prices: prices minOccurs=0 maxOccurs=unbounded
        @type prices: StorePrice
        @param version: version
        @type version: string
        @param build: build
        @type build: string
        @param release: release minOccurs=0
        @type release: Link
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        '''
        StoreEditionBase.__init__(self, itemid=itemid, deployassettype=deployassettype, itemtype=itemtype, orderassettype=orderassettype, prices=prices, version=version, build=build, release=release, itemname=itemname, resources=resources)
