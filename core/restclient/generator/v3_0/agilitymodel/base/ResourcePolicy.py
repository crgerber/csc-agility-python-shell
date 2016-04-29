from .AgilityModelBase import AgilityModelBase

class ResourcePolicyBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, trace=None, mapping=[], name=None, apiversion=None, description=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'apiVersion': {'type': 'string', 'name': 'apiversion', 'minOccurs': '0', 'native': True}, 'description': {'type': 'string', 'name': 'description', 'minOccurs': '0', 'native': True}, 'mapping': {'maxOccurs': 'unbounded', 'type': 'ResourceMapping', 'name': 'mapping', 'minOccurs': '0', 'native': False}, 'trace': {'type': 'int', 'name': 'trace', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}})
        self.trace = trace
        self.mapping = mapping
        self.name = name
        self.apiversion = apiversion
        self.description = description 
