from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class ConfigurationArtifactBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, resource=[], repository=[], documentation=None, version=None, property=[], type=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'resource': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resource', 'minOccurs': '0', 'type': 'Link'}, 'repository': {'maxOccurs': 'unbounded', 'native': False, 'name': 'repository', 'minOccurs': '0', 'type': 'Link'}, 'documentation': {'native': True, 'name': 'documentation', 'minOccurs': '0', 'type': 'string'}, 'version': {'native': True, 'name': 'version', 'minOccurs': '0', 'type': 'string'}, 'property': {'maxOccurs': 'unbounded', 'native': False, 'name': 'property', 'minOccurs': '0', 'type': 'AssetProperty'}, 'type': {'native': True, 'name': 'type', 'minOccurs': '0', 'type': 'string'}})
        self.resource = resource
        self.repository = repository
        self.documentation = documentation
        self.version = version
        self.property = property
        self.type = type 
