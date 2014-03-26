from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class NetworkServiceTypeBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, services=list(), properties=list()):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'services': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'services', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'PropertyDefinition', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.services = services
        self.properties = properties 
