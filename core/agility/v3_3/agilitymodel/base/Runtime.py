from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class RuntimeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, platformservice=None, variables=[], environment=None, properties=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'platformService': {'native': False, 'name': 'platformservice', 'minOccurs': '0', 'type': 'Link'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'environment': {'native': False, 'name': 'environment', 'minOccurs': '0', 'type': 'Link'}, 'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.platformservice = platformservice
        self.variables = variables
        self.environment = environment
        self.properties = properties 
