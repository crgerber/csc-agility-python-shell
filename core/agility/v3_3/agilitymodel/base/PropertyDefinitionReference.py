from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyDefinitionReferenceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, path=None, displayname=None, propertydefinition=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'path': {'name': 'path', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'displayName': {'name': 'displayname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'propertyDefinition': {'name': 'propertydefinition', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.path = path
        self.displayname = displayname
        self.propertydefinition = propertydefinition 
