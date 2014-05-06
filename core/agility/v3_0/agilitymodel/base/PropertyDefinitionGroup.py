from core.agility.v3_0.agilitymodel.base.Asset import AssetBase

class PropertyDefinitionGroupBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, derivedgroup=[], displayname=None, parent=None, propertydefinition=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}, 'derivedGroup': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'derivedgroup', 'minOccurs': '0', 'native': False}, 'propertyDefinition': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinition', 'name': 'propertydefinition', 'minOccurs': '0', 'native': False}, 'parent': {'type': 'Link', 'name': 'parent', 'minOccurs': '0', 'native': False}})
        self.derivedgroup = derivedgroup
        self.displayname = displayname
        self.parent = parent
        self.propertydefinition = propertydefinition 
