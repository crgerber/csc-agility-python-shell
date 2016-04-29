from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class PlatformServiceBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, topology=None, properties=[], login=None, blueprint=None, type=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'native': False, 'name': 'type', 'minOccurs': '0', 'type': 'Link'}, 'topology': {'native': False, 'name': 'topology', 'minOccurs': '0', 'type': 'Link'}, 'login': {'native': False, 'name': 'login', 'minOccurs': '0', 'type': 'Credential'}, 'blueprint': {'native': False, 'name': 'blueprint', 'minOccurs': '0', 'type': 'Link'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}})
        self.topology = topology
        self.properties = properties
        self.login = login
        self.blueprint = blueprint
        self.type = type 
