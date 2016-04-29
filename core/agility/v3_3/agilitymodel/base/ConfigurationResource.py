from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ConfigurationResourceBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, artifact=None, variable=[], property=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'artifact': {'native': False, 'name': 'artifact', 'minOccurs': '0', 'type': 'Link'}, 'variable': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variable', 'minOccurs': '0', 'type': 'PropertyDefinition'}, 'property': {'maxOccurs': 'unbounded', 'native': False, 'name': 'property', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.artifact = artifact
        self.variable = variable
        self.property = property 
