from base.StoreProduct import StoreProductBase
from actions.StoreProduct import StoreProductActions

class StoreProduct(StoreProductBase, StoreProductActions):
    '''
    classdocs
    '''
    def __init__(self, category=list(), publisher=None, itemName=None, itemType=None, releases=list(), itemDetailedPath=None, itemId=None, numReviews=None, version=None, build=None, productType=None, shortDescription=None, resources=list(), averageRating=None):
        '''
        Constructor
        @param category: category minOccurs=0 maxOccurs=unbounded
        @type category: StoreCategory
        @param publisher: publisher minOccurs=0
        @type publisher: Link
        @param itemName: itemName minOccurs=0
        @type itemName: string
        @param itemType: itemType minOccurs=0
        @type itemType: string
        @param releases: releases minOccurs=0 maxOccurs=unbounded
        @type releases: Link
        @param itemDetailedPath: itemDetailedPath minOccurs=0
        @type itemDetailedPath: string
        @param itemId: itemId
        @type itemId: int
        @param numReviews: numReviews minOccurs=0
        @type numReviews: int
        @param version: version minOccurs=0
        @type version: string
        @param build: build minOccurs=0
        @type build: string
        @param productType: productType minOccurs=0
        @type productType: Link
        @param shortDescription: shortDescription minOccurs=0
        @type shortDescription: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        @param averageRating: averageRating
        @type averageRating: decimal
        '''
        StoreProductBase.__init__(self, category=category, publisher=publisher, itemName=itemName, itemType=itemType, releases=releases, itemDetailedPath=itemDetailedPath, itemId=itemId, numReviews=numReviews, version=version, build=build, productType=productType, shortDescription=shortDescription, resources=resources, averageRating=averageRating)
