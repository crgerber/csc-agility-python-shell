from core.agility.common.AgilityModelBase import AgilityModelBase

class ArtifactRuntimeBindingBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, services=[], properties=[], runtime=None, id=None, type=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'services': {'maxOccurs': 'unbounded', 'native': True, 'name': 'services', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': False, 'name': 'type', 'minOccurs': '0', 'type': 'Link'}, 'runtime': {'native': False, 'name': 'runtime', 'minOccurs': '0', 'type': 'Link'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}})
        self.services = services
        self.properties = properties
        self.runtime = runtime
        self.id = id
        self.type = type 
