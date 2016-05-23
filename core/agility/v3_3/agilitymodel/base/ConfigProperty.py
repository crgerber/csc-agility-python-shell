from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ConfigPropertyBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, value=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'value': {'name': 'value', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.value = value 
