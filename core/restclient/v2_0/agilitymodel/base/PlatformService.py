from core.restclient.v2_0.agilitymodel.base.Item import ItemBase

class PlatformServiceBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, blueprint=None, login=None, type=None, properties=list(), topology=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'blueprint': {'type': 'Link', 'name': 'blueprint', 'minOccurs': '0', 'native': False}, 'login': {'type': 'Credential', 'name': 'login', 'minOccurs': '0', 'native': False}, 'type': {'type': 'Link', 'name': 'type', 'minOccurs': '0', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'topology': {'type': 'Link', 'name': 'topology', 'minOccurs': '0', 'native': False}})
        self.blueprint = blueprint
        self.login = login
        self.type = type
        self.properties = properties
        self.topology = topology 
