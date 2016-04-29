from core.agility.common.AgilityModelBase import AgilityModelBase

class UserTaskListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, tasks=[], totalcount=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'tasks': {'maxOccurs': 'unbounded', 'native': False, 'name': 'tasks', 'minOccurs': '0', 'type': 'UserTask'}, 'totalCount': {'native': True, 'name': 'totalcount', 'type': 'int'}})
        self.tasks = tasks
        self.totalcount = totalcount 
