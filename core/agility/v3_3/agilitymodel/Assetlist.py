from core.agility.v3_3.agilitymodel.base.Assetlist import AssetlistBase
from core.agility.v3_3.agilitymodel.actions.Assetlist import AssetlistActions

class Assetlist(AssetlistBase, AssetlistActions):
    '''
    classdocs
    '''
    def __init__(self, limit=None, name='', asset=[], totalcount=None, offset=None):
        '''
        Constructor
        @param limit: limit
        @type limit: int
        @param name: name
        @type name: string
        @param asset: asset minOccurs=0 maxOccurs=unbounded
        @type asset: Asset
        @param totalcount: totalcount
        @type totalcount: int
        @param offset: offset
        @type offset: int
        '''
        AssetlistBase.__init__(self, limit=limit, name=name, asset=asset, totalcount=totalcount, offset=offset)
