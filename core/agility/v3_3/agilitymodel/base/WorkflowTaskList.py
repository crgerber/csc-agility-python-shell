from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class WorkflowTaskListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, tasks=[], totalcount=None):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'tasks': {'maxOccurs': 'unbounded', 'native': False, 'name': 'tasks', 'minOccurs': '0', 'type': 'Link'}, 'totalCount': {'native': True, 'name': 'totalcount', 'type': 'int'}})
        self.tasks = tasks
        self.totalcount = totalcount 
