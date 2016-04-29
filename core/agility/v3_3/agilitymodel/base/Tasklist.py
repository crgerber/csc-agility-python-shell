from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class TasklistBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, limit=None, offset=None, name='', task=[], totalcount=None, parentid=None):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'limit': {'native': True, 'name': 'limit', 'type': 'int'}, 'offset': {'native': True, 'name': 'offset', 'type': 'int'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'Task': {'maxOccurs': 'unbounded', 'native': False, 'name': 'task', 'minOccurs': '0', 'type': 'Task'}, 'totalCount': {'native': True, 'name': 'totalcount', 'type': 'int'}, 'parentId': {'native': True, 'name': 'parentid', 'type': 'int'}})
        self.limit = limit
        self.offset = offset
        self.name = name
        self.task = task
        self.totalcount = totalcount
        self.parentid = parentid 
