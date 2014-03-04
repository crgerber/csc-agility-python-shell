from core.restclient.v2_0.agilitymodel.base.Item import ItemBase

class RuntimeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, environment=None, variables=list(), platformService=None, properties=list()):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'environment': {'type': 'Link', 'name': 'environment', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'platformService': {'type': 'Link', 'name': 'platformService', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.environment = environment
        self.variables = variables
        self.platformService = platformService
        self.properties = properties 
