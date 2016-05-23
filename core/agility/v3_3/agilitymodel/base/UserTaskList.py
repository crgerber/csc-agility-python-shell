from core.agility.common.AgilityModelBase import AgilityModelBase

class UserTaskListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, totalcount=None, tasks=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'totalCount': {'name': 'totalcount', 'native': True, 'type': 'int'}, 'tasks': {'name': 'tasks', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'UserTask'}})
        self.totalcount = totalcount
        self.tasks = tasks 
