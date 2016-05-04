from core.agility.v3_3.agilitymodel.base.Topology import TopologyBase

class EnvironmentBase(TopologyBase):
    '''
    classdocs
    '''
    def __init__(self, runtimes=[], type=None, private=False, deployments=[]):
        TopologyBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'deployments': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'deployments', 'minOccurs': '0', 'native': False}, 'type': {'type': 'Link', 'name': 'type', 'minOccurs': '0', 'native': False}, 'private': {'type': 'boolean', 'name': 'private', 'native': True}, 'runtimes': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'runtimes', 'minOccurs': '0', 'native': False}})
        self.runtimes = runtimes
        self.type = type
        self.private = private
        self.deployments = deployments 
