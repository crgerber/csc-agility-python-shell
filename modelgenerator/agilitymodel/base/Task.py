from AgilityModelBase import AgilityModelBase

class TaskBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, name=None, proxyUser=None, completed=None, errorMessage=None, completedTime=None, hasDependency=None, startedTime=None, user=None, parentTask=None, progress=None, type=None, id=None, result=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}, 'proxyUser': {'type': 'string', 'name': 'proxyUser', 'minOccurs': '0', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'completed': {'type': 'boolean', 'name': 'completed', 'minOccurs': '0', 'native': True}, 'errorMessage': {'type': 'string', 'name': 'errorMessage', 'minOccurs': '0', 'native': True}, 'completedTime': {'type': 'dateTime', 'name': 'completedTime', 'minOccurs': '0', 'native': True}, 'hasDependency': {'type': 'boolean', 'name': 'hasDependency', 'minOccurs': '0', 'native': True}, 'startedTime': {'type': 'dateTime', 'name': 'startedTime', 'minOccurs': '0', 'native': True}, 'user': {'type': 'string', 'name': 'user', 'minOccurs': '0', 'native': True}, 'progress': {'type': 'int', 'name': 'progress', 'minOccurs': '0', 'native': True}, 'parentTask': {'type': 'Link', 'name': 'parentTask', 'minOccurs': '0', 'native': False}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'result': {'type': 'Link', 'name': 'result', 'minOccurs': '0', 'native': False}})
        self.status = status
        self.name = name
        self.proxyUser = proxyUser
        self.completed = completed
        self.errorMessage = errorMessage
        self.completedTime = completedTime
        self.hasDependency = hasDependency
        self.startedTime = startedTime
        self.user = user
        self.parentTask = parentTask
        self.progress = progress
        self.type = type
        self.id = id
        self.result = result 
