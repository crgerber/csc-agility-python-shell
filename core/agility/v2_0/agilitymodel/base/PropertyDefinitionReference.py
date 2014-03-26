from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class PropertyDefinitionReferenceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, path=None, displayName=None, propertyDefinition=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'path': {'type': 'string', 'name': 'path', 'minOccurs': '0', 'native': True}, 'displayName': {'type': 'string', 'name': 'displayName', 'minOccurs': '0', 'native': True}, 'propertyDefinition': {'type': 'Link', 'name': 'propertyDefinition', 'minOccurs': '0', 'native': False}})
        self.path = path
        self.displayName = displayName
        self.propertyDefinition = propertyDefinition 
