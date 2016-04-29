from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PolicyTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, symbolicname='', bundleversion=''):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'symbolicName': {'native': True, 'name': 'symbolicname', 'type': 'string'}, 'bundleVersion': {'native': True, 'name': 'bundleversion', 'type': 'string'}})
        self.symbolicname = symbolicname
        self.bundleversion = bundleversion 
