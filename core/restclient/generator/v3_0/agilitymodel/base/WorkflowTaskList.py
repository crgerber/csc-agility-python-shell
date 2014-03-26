from AgilityModelBase import AgilityModelBase

class WorkflowTaskListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, totalcount=None, tasks=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'totalCount': {'type': 'int', 'name': 'totalcount', 'native': True}, 'tasks': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'tasks', 'minOccurs': '0', 'native': False}})
        self.totalcount = totalcount
        self.tasks = tasks 
