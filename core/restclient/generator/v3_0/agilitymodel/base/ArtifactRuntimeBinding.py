from AgilityModelBase import AgilityModelBase

class ArtifactRuntimeBindingBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, services=[], runtime=None, type=None, id=None, properties=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'services': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'services', 'minOccurs': '0', 'native': True}, 'runtime': {'type': 'Link', 'name': 'runtime', 'minOccurs': '0', 'native': False}, 'type': {'type': 'Link', 'name': 'type', 'minOccurs': '0', 'native': False}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.services = services
        self.runtime = runtime
        self.type = type
        self.id = id
        self.properties = properties 
