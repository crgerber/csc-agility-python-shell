from core.agility.v3_0.agilitymodel.base.Asset import AssetBase

class PropertyDefinitionReferenceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, path=None, displayname=None, propertydefinition=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'path': {'type': 'string', 'name': 'path', 'minOccurs': '0', 'native': True}, 'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}, 'propertyDefinition': {'type': 'Link', 'name': 'propertydefinition', 'minOccurs': '0', 'native': False}})
        self.path = path
        self.displayname = displayname
        self.propertydefinition = propertydefinition 
