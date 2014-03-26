from core.agility.v3_0.agilitymodel.base.Item import ItemBase

class ConfigurationArtifactBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, resource=[], repository=[], documentation=None, version=None, property=[], type=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resource': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'resource', 'minOccurs': '0', 'native': False}, 'repository': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'repository', 'minOccurs': '0', 'native': False}, 'documentation': {'type': 'string', 'name': 'documentation', 'minOccurs': '0', 'native': True}, 'version': {'type': 'string', 'name': 'version', 'minOccurs': '0', 'native': True}, 'property': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'property', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}})
        self.resource = resource
        self.repository = repository
        self.documentation = documentation
        self.version = version
        self.property = property
        self.type = type 
