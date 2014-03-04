from core.restclient.v2_0.agilitymodel.base.Item import ItemBase

class SolutionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, artifacts=list(), variables=list(), environments=list(), deployments=list(), fixedOrder=list(), anyOrder=list()):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'artifacts': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'artifacts', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'environments': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'environments', 'minOccurs': '0', 'native': False}, 'deployments': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'deployments', 'minOccurs': '0', 'native': False}, 'fixedOrder': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'fixedOrder', 'minOccurs': '0', 'native': True}, 'anyOrder': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'anyOrder', 'minOccurs': '0', 'native': True}})
        self.artifacts = artifacts
        self.variables = variables
        self.environments = environments
        self.deployments = deployments
        self.fixedOrder = fixedOrder
        self.anyOrder = anyOrder 
