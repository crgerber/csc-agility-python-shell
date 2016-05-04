from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class WorkflowTaskListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, totalcount=None, tasks=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'totalCount': {'type': 'int', 'name': 'totalcount', 'native': True}, 'tasks': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'tasks', 'minOccurs': '0', 'native': False}})
        self.totalcount = totalcount
        self.tasks = tasks 
