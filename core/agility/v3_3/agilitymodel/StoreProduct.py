from core.agility.v3_3.agilitymodel.base.StoreProduct import StoreProductBase
from core.agility.v3_3.agilitymodel.actions.StoreProduct import StoreProductActions

class StoreProduct(StoreProductBase, StoreProductActions):
    '''
    classdocs
    '''
    def __init__(self, itemdetailedpath=None, numorders=None, supportinformation=None, itemname=None, shortdescription=None, publisher=None, requirements=[], build=None, releases=[], version=None, keyfeatures=None, resources=[], category=[], itemid=None, producttype=None, itemtype=None):
        '''
        Constructor
        @param itemdetailedpath: itemdetailedpath minOccurs=0
        @type itemdetailedpath: string
        @param numorders: numorders minOccurs=0
        @type numorders: int
        @param supportinformation: supportinformation minOccurs=0
        @type supportinformation: string
        @param itemname: itemname minOccurs=0
        @type itemname: string
        @param shortdescription: shortdescription minOccurs=0
        @type shortdescription: string
        @param publisher: publisher minOccurs=0
        @type publisher: Link
        @param requirements: requirements minOccurs=0 maxOccurs=unbounded
        @type requirements: string
        @param build: build minOccurs=0
        @type build: string
        @param releases: releases minOccurs=0 maxOccurs=unbounded
        @type releases: Link
        @param version: version minOccurs=0
        @type version: string
        @param keyfeatures: keyfeatures minOccurs=0
        @type keyfeatures: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        @param category: category minOccurs=0 maxOccurs=unbounded
        @type category: StoreCategory
        @param itemid: itemid
        @type itemid: int
        @param producttype: producttype minOccurs=0
        @type producttype: Link
        @param itemtype: itemtype minOccurs=0
        @type itemtype: string
        '''
        StoreProductBase.__init__(self, itemdetailedpath=itemdetailedpath, numorders=numorders, supportinformation=supportinformation, itemname=itemname, shortdescription=shortdescription, publisher=publisher, requirements=requirements, build=build, releases=releases, version=version, keyfeatures=keyfeatures, resources=resources, category=category, itemid=itemid, producttype=producttype, itemtype=itemtype)
