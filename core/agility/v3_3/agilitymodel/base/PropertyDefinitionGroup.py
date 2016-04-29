from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyDefinitionGroupBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, parent=None, displayname=None, derivedgroup=[], propertydefinition=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'parent': {'native': False, 'name': 'parent', 'minOccurs': '0', 'type': 'Link'}, 'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}, 'derivedGroup': {'maxOccurs': 'unbounded', 'native': False, 'name': 'derivedgroup', 'minOccurs': '0', 'type': 'Link'}, 'propertyDefinition': {'maxOccurs': 'unbounded', 'native': False, 'name': 'propertydefinition', 'minOccurs': '0', 'type': 'PropertyDefinition'}})
        self.parent = parent
        self.displayname = displayname
        self.derivedgroup = derivedgroup
        self.propertydefinition = propertydefinition 
