from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ScriptPropertyReferenceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, propertydefinition=None, type=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'propertyDefinition': {'native': False, 'name': 'propertydefinition', 'minOccurs': '0', 'type': 'Link'}, 'type': {'maxOccurs': 'unbounded', 'native': False, 'name': 'type', 'minOccurs': '0', 'type': 'Link'}})
        self.propertydefinition = propertydefinition
        self.type = type 
