from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourcePolicyBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name=None, description=None, mapping=[], apiversion=None, trace=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'description': {'name': 'description', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'apiVersion': {'name': 'apiversion', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'mapping': {'name': 'mapping', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'ResourceMapping'}, 'trace': {'name': 'trace', 'native': True, 'type': 'int'}})
        self.name = name
        self.description = description
        self.mapping = mapping
        self.apiversion = apiversion
        self.trace = trace 
