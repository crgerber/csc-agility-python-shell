from core.agility.common.AgilityModelBase import AgilityModelBase


class TaskBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, name=None, proxyuser=None, completed=None, errormessage=None, completedtime=None, hasdependency=None, startedtime=None, user=None, cancelled=False, progress=None, parenttask=None, type=None, id=None, result=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}, 'proxyUser': {'type': 'string', 'name': 'proxyuser', 'minOccurs': '0', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'completed': {'type': 'boolean', 'name': 'completed', 'minOccurs': '0', 'native': True}, 'errorMessage': {'type': 'string', 'name': 'errormessage', 'minOccurs': '0', 'native': True}, 'completedTime': {'type': 'dateTime', 'name': 'completedtime', 'minOccurs': '0', 'native': True}, 'hasDependency': {'type': 'boolean', 'name': 'hasdependency', 'minOccurs': '0', 'native': True}, 'startedTime': {'type': 'dateTime', 'name': 'startedtime', 'minOccurs': '0', 'native': True}, 'user': {'type': 'string', 'name': 'user', 'minOccurs': '0', 'native': True}, 'cancelled': {'type': 'boolean', 'name': 'cancelled', 'native': True}, 'progress': {'type': 'int', 'name': 'progress', 'minOccurs': '0', 'native': True}, 'parentTask': {'type': 'Link', 'name': 'parenttask', 'minOccurs': '0', 'native': False}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'result': {'type': 'Link', 'name': 'result', 'minOccurs': '0', 'native': False}})
        self.status = status
        self.name = name
        self.proxyuser = proxyuser
        self.completed = completed
        self.errormessage = errormessage
        self.completedtime = completedtime
        self.hasdependency = hasdependency
        self.startedtime = startedtime
        self.user = user
        self.cancelled = cancelled
        self.progress = progress
        self.parenttask = parenttask
        self.type = type
        self.id = id
        self.result = result 
