from core.agility.v3_3.agilitymodel.base.Topology import TopologyBase

class ProjectBase(TopologyBase):
    '''
    classdocs
    '''
    def __init__(self, environments=[], sourceprojecttemplate=None, solution=[]):
        TopologyBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'environments': {'maxOccurs': 'unbounded', 'native': False, 'name': 'environments', 'minOccurs': '0', 'type': 'Link'}, 'sourceProjectTemplate': {'native': False, 'name': 'sourceprojecttemplate', 'minOccurs': '0', 'type': 'Link'}, 'solution': {'maxOccurs': 'unbounded', 'native': False, 'name': 'solution', 'minOccurs': '0', 'type': 'Link'}})
        self.environments = environments
        self.sourceprojecttemplate = sourceprojecttemplate
        self.solution = solution 
