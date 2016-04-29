from core.agility.v3_3.agilitymodel.base.StoreProduct import StoreProductBase
from core.agility.v3_3.agilitymodel.actions.StoreProduct import StoreProductActions

class StoreProduct(StoreProductBase, StoreProductActions):
    '''
    classdocs
    '''
    def __init__(self, keyfeatures=None, releases=[], itemtype=None, resources=[], itemid=None, shortdescription=None, supportinformation=None, category=[], producttype=None, numorders=None, itemdetailedpath=None, build=None, version=None, itemname=None, requirements=[], publisher=None):
        '''
        Constructor
        @param keyfeatures: keyfeatures minOccurs=0
        @type keyfeatures: string
        @param releases: releases minOccurs=0 maxOccurs=unbounded
        @type releases: Link
        @param itemtype: itemtype minOccurs=0
        @type itemtype: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        @param itemid: itemid
        @type itemid: int
        @param shortdescription: shortdescription minOccurs=0
        @type shortdescription: string
        @param supportinformation: supportinformation minOccurs=0
        @type supportinformation: string
        @param category: category minOccurs=0 maxOccurs=unbounded
        @type category: StoreCategory
        @param producttype: producttype minOccurs=0
        @type producttype: Link
        @param numorders: numorders minOccurs=0
        @type numorders: int
        @param itemdetailedpath: itemdetailedpath minOccurs=0
        @type itemdetailedpath: string
        @param build: build minOccurs=0
        @type build: string
        @param version: version minOccurs=0
        @type version: string
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param requirements: requirements minOccurs=0 maxOccurs=unbounded
        @type requirements: string
        @param publisher: publisher minOccurs=0
        @type publisher: Link
        '''
        StoreProductBase.__init__(self, keyfeatures=keyfeatures, releases=releases, itemtype=itemtype, resources=resources, itemid=itemid, shortdescription=shortdescription, supportinformation=supportinformation, category=category, producttype=producttype, numorders=numorders, itemdetailedpath=itemdetailedpath, build=build, version=version, itemname=itemname, requirements=requirements, publisher=publisher)
