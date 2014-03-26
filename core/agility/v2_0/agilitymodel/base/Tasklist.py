from core.agility.common.AgilityModelBase import AgilityModelBase


class TasklistBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, Task=list(), name='', offset=None, totalCount=None, limit=None, parentId=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'Task': {'maxOccurs': 'unbounded', 'type': 'Task', 'name': 'Task', 'minOccurs': '0', 'native': False}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'offset': {'type': 'int', 'name': 'offset', 'native': True}, 'totalCount': {'type': 'int', 'name': 'totalCount', 'native': True}, 'limit': {'type': 'int', 'name': 'limit', 'native': True}, 'parentId': {'type': 'int', 'name': 'parentId', 'native': True}})
        self.Task = Task
        self.name = name
        self.offset = offset
        self.totalCount = totalCount
        self.limit = limit
        self.parentId = parentId 
