from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ConfigurationResourceBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, variable=[], artifact=None, property=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'variable': {'name': 'variable', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PropertyDefinition'}, 'artifact': {'name': 'artifact', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'property': {'name': 'property', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.variable = variable
        self.artifact = artifact
        self.property = property 
