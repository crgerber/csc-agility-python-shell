from base.AssetTypeList import AssetTypeListBase
from actions.AssetTypeList import AssetTypeListActions

class AssetTypeList(AssetTypeListBase, AssetTypeListActions):
    '''
    classdocs
    '''
    def __init__(self, assettype=[]):
        '''
        Constructor
        @param assettype: assettype minOccurs=0 maxOccurs=unbounded
        @type assettype: AssetType
        '''
        AssetTypeListBase.__init__(self, assettype=assettype)
