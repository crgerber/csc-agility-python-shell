from base.LifecyclePolicyMeta import LifecyclePolicyMetaBase
from actions.LifecyclePolicyMeta import LifecyclePolicyMetaActions

class LifecyclePolicyMeta(LifecyclePolicyMetaBase, LifecyclePolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self, supportedAssetType=list()):
        '''
        Constructor
        @param supportedAssetType: supportedAssetType minOccurs=0 maxOccurs=unbounded
        @type supportedAssetType: AssetTypeMeta
        '''
        LifecyclePolicyMetaBase.__init__(self, supportedAssetType=supportedAssetType)
