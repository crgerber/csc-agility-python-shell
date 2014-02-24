from PolicyMeta import PolicyMetaBase

class LifecyclePolicyMetaBase(PolicyMetaBase):
    '''
    classdocs
    '''
    def __init__(self, supportedAssetType=list()):
        PolicyMetaBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'supportedAssetType': {'maxOccurs': 'unbounded', 'type': 'AssetTypeMeta', 'name': 'supportedAssetType', 'minOccurs': '0', 'native': False}})
        self.supportedAssetType = supportedAssetType 
