from Asset import AssetBase

class PropertyDefinitionGroupBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, derivedGroup=list(), displayName=None, parent=None, propertyDefinition=list()):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayName', 'minOccurs': '0', 'native': True}, 'derivedGroup': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'derivedGroup', 'minOccurs': '0', 'native': False}, 'propertyDefinition': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinition', 'name': 'propertyDefinition', 'minOccurs': '0', 'native': False}, 'parent': {'type': 'Link', 'name': 'parent', 'minOccurs': '0', 'native': False}})
        self.derivedGroup = derivedGroup
        self.displayName = displayName
        self.parent = parent
        self.propertyDefinition = propertyDefinition 
