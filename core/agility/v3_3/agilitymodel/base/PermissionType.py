from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PermissionTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, global_=None, displayname=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'global': {'native': True, 'name': 'global_', 'minOccurs': '0', 'type': 'boolean'}, 'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}})
        self.global_ = global_
        self.displayname = displayname 
