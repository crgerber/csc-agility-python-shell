from core.agility.v3_3.agilitymodel.base.StoreRelease import StoreReleaseBase
from core.agility.v3_3.agilitymodel.actions.StoreRelease import StoreReleaseActions

class StoreRelease(StoreReleaseBase, StoreReleaseActions):
    '''
    classdocs
    '''
    def __init__(self, build='', resources=[], version='', editions=[], product=None):
        '''
        Constructor
        @param build: build
        @type build: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        @param version: version
        @type version: string
        @param editions: editions minOccurs=0 maxOccurs=unbounded
        @type editions: Link
        @param product: product minOccurs=0
        @type product: Link
        '''
        StoreReleaseBase.__init__(self, build=build, resources=resources, version=version, editions=editions, product=product)
