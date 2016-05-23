from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class WorkflowTaskListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, totalcount=None, tasks=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'totalCount': {'name': 'totalcount', 'native': True, 'type': 'int'}, 'tasks': {'name': 'tasks', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.totalcount = totalcount
        self.tasks = tasks 
