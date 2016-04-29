from .Asset import AssetBase

class PolicyTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, bundleversion='', symbolicname=''):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'bundleVersion': {'type': 'string', 'name': 'bundleversion', 'native': True}, 'symbolicName': {'type': 'string', 'name': 'symbolicname', 'native': True}})
        self.bundleversion = bundleversion
        self.symbolicname = symbolicname 
