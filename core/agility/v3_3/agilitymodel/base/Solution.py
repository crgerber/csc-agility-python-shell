from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class SolutionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, environments=[], variables=[], fixedorder=[], anyorder=[], artifacts=[], deployments=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'environments': {'name': 'environments', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'variables': {'name': 'variables', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'fixedOrder': {'name': 'fixedorder', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'anyOrder': {'name': 'anyorder', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'artifacts': {'name': 'artifacts', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'deployments': {'name': 'deployments', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.environments = environments
        self.variables = variables
        self.fixedorder = fixedorder
        self.anyorder = anyorder
        self.artifacts = artifacts
        self.deployments = deployments 
