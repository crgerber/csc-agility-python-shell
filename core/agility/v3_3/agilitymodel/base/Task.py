from core.agility.common.AgilityModelBase import AgilityModelBase

class TaskBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, workitemid=None, paused=None, type=None, parenttask=None, completed=None, status=None, id=None, user=None, progress=None, cancellable=None, startedtime=None, cancelled=False, completedtime=None, pausedtime=None, name=None, pausedworkitemid=None, result=None, currentnodeid=None, currentnodename=None, visible=False, hasdependency=None, proxyuser=None, errormessage=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'workItemId': {'name': 'workitemid', 'minOccurs': '0', 'native': True, 'type': 'long'}, 'startedTime': {'name': 'startedtime', 'minOccurs': '0', 'native': True, 'type': 'dateTime'}, 'paused': {'name': 'paused', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'parentTask': {'name': 'parenttask', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'completed': {'name': 'completed', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'user': {'name': 'user', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'currentNodeId': {'name': 'currentnodeid', 'minOccurs': '0', 'native': True, 'type': 'long'}, 'cancellable': {'name': 'cancellable', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'pausedTime': {'name': 'pausedtime', 'minOccurs': '0', 'native': True, 'type': 'dateTime'}, 'completedTime': {'name': 'completedtime', 'minOccurs': '0', 'native': True, 'type': 'dateTime'}, 'cancelled': {'name': 'cancelled', 'native': True, 'type': 'boolean'}, 'name': {'name': 'name', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'pausedWorkItemId': {'name': 'pausedworkitemid', 'minOccurs': '0', 'native': True, 'type': 'long'}, 'result': {'name': 'result', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'progress': {'name': 'progress', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'currentNodeName': {'name': 'currentnodename', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'visible': {'name': 'visible', 'native': True, 'type': 'boolean'}, 'hasDependency': {'name': 'hasdependency', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'proxyUser': {'name': 'proxyuser', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'errorMessage': {'name': 'errormessage', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.workitemid = workitemid
        self.paused = paused
        self.type = type
        self.parenttask = parenttask
        self.completed = completed
        self.status = status
        self.id = id
        self.user = user
        self.progress = progress
        self.cancellable = cancellable
        self.startedtime = startedtime
        self.cancelled = cancelled
        self.completedtime = completedtime
        self.pausedtime = pausedtime
        self.name = name
        self.pausedworkitemid = pausedworkitemid
        self.result = result
        self.currentnodeid = currentnodeid
        self.currentnodename = currentnodename
        self.visible = visible
        self.hasdependency = hasdependency
        self.proxyuser = proxyuser
        self.errormessage = errormessage 
