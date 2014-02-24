from Asset import AssetBase

class PolicyTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, bundleVersion='', symbolicName=''):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'bundleVersion': {'type': 'string', 'name': 'bundleVersion', 'native': True}, 'symbolicName': {'type': 'string', 'name': 'symbolicName', 'native': True}})
        self.bundleVersion = bundleVersion
        self.symbolicName = symbolicName 
