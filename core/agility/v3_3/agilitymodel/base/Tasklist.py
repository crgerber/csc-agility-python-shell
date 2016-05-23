from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class TasklistBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, task=[], totalcount=None, parentid=None, name='', limit=None, offset=None):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'Task': {'name': 'task', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Task'}, 'totalCount': {'name': 'totalcount', 'native': True, 'type': 'int'}, 'parentId': {'name': 'parentid', 'native': True, 'type': 'int'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'limit': {'name': 'limit', 'native': True, 'type': 'int'}, 'offset': {'name': 'offset', 'native': True, 'type': 'int'}})
        self.task = task
        self.totalcount = totalcount
        self.parentid = parentid
        self.name = name
        self.limit = limit
        self.offset = offset 
