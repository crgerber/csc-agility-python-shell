from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyDefinitionReferenceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, path=None, displayname=None, propertydefinition=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'path': {'native': True, 'name': 'path', 'minOccurs': '0', 'type': 'string'}, 'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}, 'propertyDefinition': {'native': False, 'name': 'propertydefinition', 'minOccurs': '0', 'type': 'Link'}})
        self.path = path
        self.displayname = displayname
        self.propertydefinition = propertydefinition 
