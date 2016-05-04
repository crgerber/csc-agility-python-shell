from core.agility.common.AgilityModelBase import AgilityModelBase

class UserTaskListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, totalcount=None, tasks=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'totalCount': {'type': 'int', 'name': 'totalcount', 'native': True}, 'tasks': {'maxOccurs': 'unbounded', 'type': 'UserTask', 'name': 'tasks', 'minOccurs': '0', 'native': False}})
        self.totalcount = totalcount
        self.tasks = tasks 
