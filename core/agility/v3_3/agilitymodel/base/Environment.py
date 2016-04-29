from core.agility.v3_3.agilitymodel.base.Topology import TopologyBase

class EnvironmentBase(TopologyBase):
    '''
    classdocs
    '''
    def __init__(self, private=False, deployments=[], runtimes=[], type=None):
        TopologyBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'private': {'native': True, 'name': 'private', 'type': 'boolean'}, 'deployments': {'maxOccurs': 'unbounded', 'native': False, 'name': 'deployments', 'minOccurs': '0', 'type': 'Link'}, 'type': {'native': False, 'name': 'type', 'minOccurs': '0', 'type': 'Link'}, 'runtimes': {'maxOccurs': 'unbounded', 'native': False, 'name': 'runtimes', 'minOccurs': '0', 'type': 'Link'}})
        self.private = private
        self.deployments = deployments
        self.runtimes = runtimes
        self.type = type 
