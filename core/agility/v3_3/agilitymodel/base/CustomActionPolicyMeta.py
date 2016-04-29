from core.agility.v3_3.agilitymodel.base.PolicyMeta import PolicyMetaBase

class CustomActionPolicyMetaBase(PolicyMetaBase):
    '''
    classdocs
    '''
    def __init__(self, supportedassettype=[]):
        PolicyMetaBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'supportedAssetType': {'maxOccurs': 'unbounded', 'native': False, 'name': 'supportedassettype', 'minOccurs': '0', 'type': 'AssetTypeMeta'}})
        self.supportedassettype = supportedassettype 
