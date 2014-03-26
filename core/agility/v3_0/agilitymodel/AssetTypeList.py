from core.agility.v3_0.agilitymodel.base.AssetTypeList import AssetTypeListBase
from core.agility.v3_0.agilitymodel.actions.AssetTypeList import AssetTypeListActions

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
