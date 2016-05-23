from core.agility.v3_3.agilitymodel.base.StoreRelease import StoreReleaseBase
from core.agility.v3_3.agilitymodel.actions.StoreRelease import StoreReleaseActions

class StoreRelease(StoreReleaseBase, StoreReleaseActions):
    '''
    classdocs
    '''
    def __init__(self, product=None, editions=[], resources=[], build='', version=''):
        '''
        Constructor
        @param product: product minOccurs=0
        @type product: Link
        @param editions: editions minOccurs=0 maxOccurs=unbounded
        @type editions: Link
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        @param build: build
        @type build: string
        @param version: version
        @type version: string
        '''
        StoreReleaseBase.__init__(self, product=product, editions=editions, resources=resources, build=build, version=version)
