from base.AssetTypeList import AssetTypeListBase
from actions.AssetTypeList import AssetTypeListActions

class AssetTypeList(AssetTypeListBase, AssetTypeListActions):
    '''
    classdocs
    '''
    def __init__(self, assetType=list()):
        '''
        Constructor
        @param assetType: assetType minOccurs=0 maxOccurs=unbounded
        @type assetType: AssetType
        '''
        AssetTypeListBase.__init__(self, assetType=assetType)
