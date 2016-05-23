from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class RuntimeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, environment=None, variables=[], platformservice=None, properties=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'environment': {'name': 'environment', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'platformService': {'name': 'platformservice', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'variables': {'name': 'variables', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}})
        self.environment = environment
        self.variables = variables
        self.platformservice = platformservice
        self.properties = properties 
