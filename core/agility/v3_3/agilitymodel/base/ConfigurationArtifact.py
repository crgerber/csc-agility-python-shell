from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ConfigurationArtifactBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, property=[], documentation=None, version=None, repository=[], type=None, resource=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'property': {'name': 'property', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'documentation': {'name': 'documentation', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'version': {'name': 'version', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'repository': {'name': 'repository', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'resource': {'name': 'resource', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.property = property
        self.documentation = documentation
        self.version = version
        self.repository = repository
        self.type = type
        self.resource = resource 
