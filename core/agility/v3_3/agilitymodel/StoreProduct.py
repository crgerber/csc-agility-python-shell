from base.StoreProduct import StoreProductBase
from actions.StoreProduct import StoreProductActions

class StoreProduct(StoreProductBase, StoreProductActions):
    '''
    classdocs
    '''
    def __init__(self, category=[], publisher=None, numorders=None, keyfeatures=None, requirements=[], itemtype=None, releases=[], itemdetailedpath=None, itemid=None, version=None, build=None, producttype=None, supportinformation=None, shortdescription=None, itemname=None, resources=[]):
        '''
        Constructor
        @param category: category minOccurs=0 maxOccurs=unbounded
        @type category: StoreCategory
        @param publisher: publisher minOccurs=0
        @type publisher: Link
        @param numorders: numorders minOccurs=0
        @type numorders: int
        @param keyfeatures: keyfeatures minOccurs=0
        @type keyfeatures: string
        @param requirements: requirements minOccurs=0 maxOccurs=unbounded
        @type requirements: string
        @param itemtype: itemtype minOccurs=0
        @type itemtype: string
        @param releases: releases minOccurs=0 maxOccurs=unbounded
        @type releases: Link
        @param itemdetailedpath: itemdetailedpath minOccurs=0
        @type itemdetailedpath: string
        @param itemid: itemid
        @type itemid: int
        @param version: version minOccurs=0
        @type version: string
        @param build: build minOccurs=0
        @type build: string
        @param producttype: producttype minOccurs=0
        @type producttype: Link
        @param supportinformation: supportinformation minOccurs=0
        @type supportinformation: string
        @param shortdescription: shortdescription minOccurs=0
        @type shortdescription: string
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        '''
        StoreProductBase.__init__(self, category=category, publisher=publisher, numorders=numorders, keyfeatures=keyfeatures, requirements=requirements, itemtype=itemtype, releases=releases, itemdetailedpath=itemdetailedpath, itemid=itemid, version=version, build=build, producttype=producttype, supportinformation=supportinformation, shortdescription=shortdescription, itemname=itemname, resources=resources)
