from base.Assetlist import AssetlistBase
from actions.Assetlist import AssetlistActions

class Assetlist(AssetlistBase, AssetlistActions):
    '''
    classdocs
    '''
    def __init__(self, totalCount=None, offset=None, limit=None, Asset=list(), name=''):
        '''
        Constructor
        @param totalCount: totalCount
        @type totalCount: int
        @param offset: offset
        @type offset: int
        @param limit: limit
        @type limit: int
        @param Asset: Asset minOccurs=0 maxOccurs=unbounded
        @type Asset: Asset
        @param name: name
        @type name: string
        '''
        AssetlistBase.__init__(self, totalCount=totalCount, offset=offset, limit=limit, Asset=Asset, name=name)
