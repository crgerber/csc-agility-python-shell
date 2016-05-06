from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PermissionTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, global_=None, displayname=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'global': {'type': 'boolean', 'name': 'global_', 'minOccurs': '0', 'native': True}, 'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}})
        self.global_ = global_
        self.displayname = displayname 
