from Item import ItemBase

class ConfigurationResourceBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, variable=list(), property=list(), artifact=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variable': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinition', 'name': 'variable', 'minOccurs': '0', 'native': False}, 'property': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'property', 'minOccurs': '0', 'native': False}, 'artifact': {'type': 'Link', 'name': 'artifact', 'minOccurs': '0', 'native': False}})
        self.variable = variable
        self.property = property
        self.artifact = artifact 
