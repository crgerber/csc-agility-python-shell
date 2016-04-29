from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourcePolicyBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, apiversion=None, name=None, trace=None, mapping=[], description=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'apiVersion': {'native': True, 'name': 'apiversion', 'minOccurs': '0', 'type': 'string'}, 'name': {'native': True, 'name': 'name', 'minOccurs': '0', 'type': 'string'}, 'trace': {'native': True, 'name': 'trace', 'type': 'int'}, 'mapping': {'maxOccurs': 'unbounded', 'native': False, 'name': 'mapping', 'minOccurs': '0', 'type': 'ResourceMapping'}, 'description': {'native': True, 'name': 'description', 'minOccurs': '0', 'type': 'string'}})
        self.apiversion = apiversion
        self.name = name
        self.trace = trace
        self.mapping = mapping
        self.description = description 
