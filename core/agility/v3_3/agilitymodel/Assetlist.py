from core.agility.v3_3.agilitymodel.base.Assetlist import AssetlistBase
from core.agility.v3_3.agilitymodel.actions.Assetlist import AssetlistActions

class Assetlist(AssetlistBase, AssetlistActions):
    '''
    classdocs
    '''
    def __init__(self, name='', totalcount=None, limit=None, offset=None, asset=[]):
        '''
        Constructor
        @param name: name
        @type name: string
        @param totalcount: totalcount
        @type totalcount: int
        @param limit: limit
        @type limit: int
        @param offset: offset
        @type offset: int
        @param asset: asset minOccurs=0 maxOccurs=unbounded
        @type asset: Asset
        '''
        AssetlistBase.__init__(self, name=name, totalcount=totalcount, limit=limit, offset=offset, asset=asset)
