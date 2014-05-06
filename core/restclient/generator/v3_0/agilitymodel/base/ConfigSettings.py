from Asset import AssetBase

class ConfigSettingsBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, property=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'property': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'property', 'minOccurs': '0', 'native': False}})
        self.property = property 
