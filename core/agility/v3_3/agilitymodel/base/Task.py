from core.agility.common.AgilityModelBase import AgilityModelBase

class TaskBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, workitemid=None, parenttask=None, paused=None, visible=False, result=None, id=None, pausedworkitemid=None, completedtime=None, startedtime=None, progress=None, type=None, status=None, completed=None, errormessage=None, hasdependency=None, user=None, currentnodeid=None, name=None, proxyuser=None, cancellable=None, pausedtime=None, cancelled=False, currentnodename=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'pausedTime': {'type': 'dateTime', 'name': 'pausedtime', 'minOccurs': '0', 'native': True}, 'parentTask': {'type': 'Link', 'name': 'parenttask', 'minOccurs': '0', 'native': False}, 'paused': {'type': 'boolean', 'name': 'paused', 'minOccurs': '0', 'native': True}, 'visible': {'type': 'boolean', 'name': 'visible', 'native': True}, 'result': {'type': 'Link', 'name': 'result', 'minOccurs': '0', 'native': False}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'pausedWorkItemId': {'type': 'long', 'name': 'pausedworkitemid', 'minOccurs': '0', 'native': True}, 'completedTime': {'type': 'dateTime', 'name': 'completedtime', 'minOccurs': '0', 'native': True}, 'startedTime': {'type': 'dateTime', 'name': 'startedtime', 'minOccurs': '0', 'native': True}, 'progress': {'type': 'int', 'name': 'progress', 'minOccurs': '0', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'completed': {'type': 'boolean', 'name': 'completed', 'minOccurs': '0', 'native': True}, 'errorMessage': {'type': 'string', 'name': 'errormessage', 'minOccurs': '0', 'native': True}, 'hasDependency': {'type': 'boolean', 'name': 'hasdependency', 'minOccurs': '0', 'native': True}, 'user': {'type': 'string', 'name': 'user', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}, 'currentNodeId': {'type': 'long', 'name': 'currentnodeid', 'minOccurs': '0', 'native': True}, 'proxyUser': {'type': 'string', 'name': 'proxyuser', 'minOccurs': '0', 'native': True}, 'cancellable': {'type': 'boolean', 'name': 'cancellable', 'minOccurs': '0', 'native': True}, 'workItemId': {'type': 'long', 'name': 'workitemid', 'minOccurs': '0', 'native': True}, 'cancelled': {'type': 'boolean', 'name': 'cancelled', 'native': True}, 'currentNodeName': {'type': 'string', 'name': 'currentnodename', 'minOccurs': '0', 'native': True}})
        self.workitemid = workitemid
        self.parenttask = parenttask
        self.paused = paused
        self.visible = visible
        self.result = result
        self.id = id
        self.pausedworkitemid = pausedworkitemid
        self.completedtime = completedtime
        self.startedtime = startedtime
        self.progress = progress
        self.type = type
        self.status = status
        self.completed = completed
        self.errormessage = errormessage
        self.hasdependency = hasdependency
        self.user = user
        self.currentnodeid = currentnodeid
        self.name = name
        self.proxyuser = proxyuser
        self.cancellable = cancellable
        self.pausedtime = pausedtime
        self.cancelled = cancelled
        self.currentnodename = currentnodename 
