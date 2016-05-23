from core.agility.common.AgilityModelBase import AgilityModelBase

class ArtifactRuntimeBindingBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, id=None, services=[], type=None, runtime=None, properties=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'id': {'name': 'id', 'native': True, 'type': 'int'}, 'services': {'name': 'services', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'runtime': {'name': 'runtime', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}})
        self.id = id
        self.services = services
        self.type = type
        self.runtime = runtime
        self.properties = properties 
