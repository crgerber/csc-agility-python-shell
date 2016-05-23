from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyDefinitionGroupBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, derivedgroup=[], displayname=None, propertydefinition=[], parent=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'name': 'displayname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'derivedGroup': {'name': 'derivedgroup', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'propertyDefinition': {'name': 'propertydefinition', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PropertyDefinition'}, 'parent': {'name': 'parent', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.derivedgroup = derivedgroup
        self.displayname = displayname
        self.propertydefinition = propertydefinition
        self.parent = parent 
