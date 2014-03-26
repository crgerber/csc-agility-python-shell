from core.agility.v3_0.agilitymodel.base.StoreRelease import StoreReleaseBase
from core.agility.v3_0.agilitymodel.actions.StoreRelease import StoreReleaseActions

class StoreRelease(StoreReleaseBase, StoreReleaseActions):
    '''
    classdocs
    '''
    def __init__(self, editions=[], product=None, version='', build='', resources=[]):
        '''
        Constructor
        @param editions: editions minOccurs=0 maxOccurs=unbounded
        @type editions: Link
        @param product: product minOccurs=0
        @type product: Link
        @param version: version
        @type version: string
        @param build: build
        @type build: string
        @param resources: resources minOccurs=0 maxOccurs=unbounded
        @type resources: StoreResource
        '''
        StoreReleaseBase.__init__(self, editions=editions, product=product, version=version, build=build, resources=resources)
