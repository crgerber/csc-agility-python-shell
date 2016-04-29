from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class SolutionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, deployments=[], anyorder=[], environments=[], artifacts=[], fixedorder=[], variables=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'deployments': {'maxOccurs': 'unbounded', 'native': False, 'name': 'deployments', 'minOccurs': '0', 'type': 'Link'}, 'artifacts': {'maxOccurs': 'unbounded', 'native': False, 'name': 'artifacts', 'minOccurs': '0', 'type': 'Link'}, 'environments': {'maxOccurs': 'unbounded', 'native': False, 'name': 'environments', 'minOccurs': '0', 'type': 'Link'}, 'anyOrder': {'maxOccurs': 'unbounded', 'native': True, 'name': 'anyorder', 'minOccurs': '0', 'type': 'string'}, 'fixedOrder': {'maxOccurs': 'unbounded', 'native': True, 'name': 'fixedorder', 'minOccurs': '0', 'type': 'string'}, 'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'AssetProperty'}})
        self.deployments = deployments
        self.anyorder = anyorder
        self.environments = environments
        self.artifacts = artifacts
        self.fixedorder = fixedorder
        self.variables = variables 
