from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PolicyTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, bundleversion='', symbolicname=''):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'bundleVersion': {'name': 'bundleversion', 'native': True, 'type': 'string'}, 'symbolicName': {'name': 'symbolicname', 'native': True, 'type': 'string'}})
        self.bundleversion = bundleversion
        self.symbolicname = symbolicname 
