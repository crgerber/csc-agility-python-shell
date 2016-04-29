from .PolicyMeta import PolicyMetaBase

class LifecyclePolicyMetaBase(PolicyMetaBase):
    '''
    classdocs
    '''
    def __init__(self, supportedassettype=[]):
        PolicyMetaBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'supportedAssetType': {'maxOccurs': 'unbounded', 'type': 'AssetTypeMeta', 'name': 'supportedassettype', 'minOccurs': '0', 'native': False}})
        self.supportedassettype = supportedassettype 
