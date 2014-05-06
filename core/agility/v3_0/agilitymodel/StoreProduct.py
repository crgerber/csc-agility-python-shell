from core.agility.v3_0.agilitymodel.base.StoreProduct import StoreProductBase
from core.agility.v3_0.agilitymodel.actions.StoreProduct import StoreProductActions

class StoreProduct(StoreProductBase, StoreProductActions):
    '''
    classdocs
    '''
    def __init__(self, category=[], publisher=None, itemname=None, itemtype=None, releases=[], itemdetailedpath=None, itemid=None, numreviews=None, version=None, build=None, producttype=None, shortdescription=None, resources=[], averagerating=None):
        '''
        Constructor
        @param category: category minOccurs=0 maxOccurs=unbounded
        @type category: StoreCategory
        @param publisher: publisher minOccurs=0
        @type publisher: Link
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param itemtype: itemtype minOccurs=0
        @type itemtype: string
        @param releases: releases minOccurs=0 maxOccurs=unbounded
        @type releases: Link
        @param itemdetailedpath: itemdetailedpath minOccurs=0
        @type itemdetailedpath: string
        @param itemid: itemid
        @type itemid: int
        @param numreviews: numreviews minOccurs=0
        @type numreviews: int
        @param version: version minOccurs=0
        @type version: string
        @param build: build minOccurs=0
        @type build: string
        @param producttype: producttype minOccurs=0
        @type producttype: Link
        @param shortdescription: shortdescription minOccurs=0
        @type shortdescription: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        @param averagerating: averagerating
        @type averagerating: decimal
        '''
        StoreProductBase.__init__(self, category=category, publisher=publisher, itemname=itemname, itemtype=itemtype, releases=releases, itemdetailedpath=itemdetailedpath, itemid=itemid, numreviews=numreviews, version=version, build=build, producttype=producttype, shortdescription=shortdescription, resources=resources, averagerating=averagerating)
