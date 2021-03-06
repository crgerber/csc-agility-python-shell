from Item import ItemBase

class SolutionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, artifacts=[], variables=[], environments=[], deployments=[], fixedorder=[], anyorder=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'artifacts': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'artifacts', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'environments': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'environments', 'minOccurs': '0', 'native': False}, 'deployments': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'deployments', 'minOccurs': '0', 'native': False}, 'fixedOrder': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'fixedorder', 'minOccurs': '0', 'native': True}, 'anyOrder': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'anyorder', 'minOccurs': '0', 'native': True}})
        self.artifacts = artifacts
        self.variables = variables
        self.environments = environments
        self.deployments = deployments
        self.fixedorder = fixedorder
        self.anyorder = anyorder 
