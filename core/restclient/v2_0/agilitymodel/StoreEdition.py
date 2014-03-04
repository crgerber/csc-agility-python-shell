from core.restclient.v2_0.agilitymodel.base.StoreEdition import StoreEditionBase
from core.restclient.v2_0.agilitymodel.actions.StoreEdition import StoreEditionActions

class StoreEdition(StoreEditionBase, StoreEditionActions):
    '''
    classdocs
    '''
    def __init__(self, itemId=None, itemType=None, prices=list(), version='', build='', release=None, itemName=None, resources=list()):
        '''
        Constructor
        @param itemId: itemId minOccurs=0
        @type itemId: int
        @param itemType: itemType minOccurs=0
        @type itemType: string
        @param prices: prices minOccurs=0 maxOccurs=unbounded
        @type prices: StorePrice
        @param version: version
        @type version: string
        @param build: build
        @type build: string
        @param release: release minOccurs=0
        @type release: Link
        @param itemName: itemName minOccurs=0
        @type itemName: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        '''
        StoreEditionBase.__init__(self, itemId=itemId, itemType=itemType, prices=prices, version=version, build=build, release=release, itemName=itemName, resources=resources)
