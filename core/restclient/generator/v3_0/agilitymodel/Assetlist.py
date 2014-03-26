from base.Assetlist import AssetlistBase
from actions.Assetlist import AssetlistActions

class Assetlist(AssetlistBase, AssetlistActions):
    '''
    classdocs
    '''
    def __init__(self, totalcount=None, offset=None, limit=None, asset=[], name=''):
        '''
        Constructor
        @param totalcount: totalcount
        @type totalcount: int
        @param offset: offset
        @type offset: int
        @param limit: limit
        @type limit: int
        @param asset: asset minOccurs=0 maxOccurs=unbounded
        @type asset: Asset
        @param name: name
        @type name: string
        '''
        AssetlistBase.__init__(self, totalcount=totalcount, offset=offset, limit=limit, asset=asset, name=name)
