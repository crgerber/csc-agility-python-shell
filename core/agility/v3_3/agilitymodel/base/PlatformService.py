from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class PlatformServiceBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, topology=None, blueprint=None, properties=[], type=None, login=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'topology': {'name': 'topology', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'blueprint': {'name': 'blueprint', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'login': {'name': 'login', 'minOccurs': '0', 'native': False, 'type': 'Credential'}})
        self.topology = topology
        self.blueprint = blueprint
        self.properties = properties
        self.type = type
        self.login = login 
