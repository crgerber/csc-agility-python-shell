from core.agility.v3_0.agilitymodel.base.AssetProperty import AssetPropertyBase

class ForeignAssetPropertyBase(AssetPropertyBase):
    '''
    classdocs
    '''
    def __init__(self, propertydefinitionreference=None):
        AssetPropertyBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'propertyDefinitionReference': {'type': 'Link', 'name': 'propertydefinitionreference', 'minOccurs': '0', 'native': False}})
        self.propertydefinitionreference = propertydefinitionreference 
