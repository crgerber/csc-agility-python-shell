from core.agility.v3_3.agilitymodel.base.Topology import TopologyBase

class EnvironmentBase(TopologyBase):
    '''
    classdocs
    '''
    def __init__(self, private=False, runtimes=[], type=None, deployments=[]):
        TopologyBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'private': {'name': 'private', 'native': True, 'type': 'boolean'}, 'runtimes': {'name': 'runtimes', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'deployments': {'name': 'deployments', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.private = private
        self.runtimes = runtimes
        self.type = type
        self.deployments = deployments 
