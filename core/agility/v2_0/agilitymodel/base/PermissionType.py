from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class PermissionTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, global_=None, displayName=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'global': {'type': 'boolean', 'name': 'global_', 'minOccurs': '0', 'native': True}, 'displayName': {'type': 'string', 'name': 'displayName', 'minOccurs': '0', 'native': True}})
        self.global_ = global_
        self.displayName = displayName 
