from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ConfigSettingsBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, property=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'property': {'maxOccurs': 'unbounded', 'native': False, 'name': 'property', 'minOccurs': '0', 'type': 'Link'}})
        self.property = property 
