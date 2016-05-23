from core.agility.v3_3.agilitymodel.base.Topology import TopologyBase

class ProjectBase(TopologyBase):
    '''
    classdocs
    '''
    def __init__(self, environments=[], sourceprojecttemplate=None, solution=[]):
        TopologyBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'environments': {'name': 'environments', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'sourceProjectTemplate': {'name': 'sourceprojecttemplate', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'solution': {'name': 'solution', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.environments = environments
        self.sourceprojecttemplate = sourceprojecttemplate
        self.solution = solution 
