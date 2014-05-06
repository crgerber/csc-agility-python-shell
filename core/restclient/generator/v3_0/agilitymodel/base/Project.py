from Topology import TopologyBase

class ProjectBase(TopologyBase):
    '''
    classdocs
    '''
    def __init__(self, solution=[], environments=[]):
        TopologyBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'solution': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'solution', 'minOccurs': '0', 'native': False}, 'environments': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'environments', 'minOccurs': '0', 'native': False}})
        self.solution = solution
        self.environments = environments 
