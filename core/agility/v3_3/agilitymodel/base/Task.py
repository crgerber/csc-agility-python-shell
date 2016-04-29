from core.agility.common.AgilityModelBase import AgilityModelBase

class TaskBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, cancellable=None, pausedtime=None, user=None, status=None, type=None, errormessage=None, workitemid=None, paused=None, result=None, name=None, proxyuser=None, cancelled=False, completed=None, startedtime=None, visible=False, currentnodeid=None, hasdependency=None, progress=None, id=None, parenttask=None, completedtime=None, pausedworkitemid=None, currentnodename=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cancellable': {'native': True, 'name': 'cancellable', 'minOccurs': '0', 'type': 'boolean'}, 'pausedTime': {'native': True, 'name': 'pausedtime', 'minOccurs': '0', 'type': 'dateTime'}, 'user': {'native': True, 'name': 'user', 'minOccurs': '0', 'type': 'string'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': True, 'name': 'type', 'minOccurs': '0', 'type': 'string'}, 'errorMessage': {'native': True, 'name': 'errormessage', 'minOccurs': '0', 'type': 'string'}, 'workItemId': {'native': True, 'name': 'workitemid', 'minOccurs': '0', 'type': 'long'}, 'paused': {'native': True, 'name': 'paused', 'minOccurs': '0', 'type': 'boolean'}, 'result': {'native': False, 'name': 'result', 'minOccurs': '0', 'type': 'Link'}, 'name': {'native': True, 'name': 'name', 'minOccurs': '0', 'type': 'string'}, 'proxyUser': {'native': True, 'name': 'proxyuser', 'minOccurs': '0', 'type': 'string'}, 'cancelled': {'native': True, 'name': 'cancelled', 'type': 'boolean'}, 'completed': {'native': True, 'name': 'completed', 'minOccurs': '0', 'type': 'boolean'}, 'startedTime': {'native': True, 'name': 'startedtime', 'minOccurs': '0', 'type': 'dateTime'}, 'visible': {'native': True, 'name': 'visible', 'type': 'boolean'}, 'currentNodeId': {'native': True, 'name': 'currentnodeid', 'minOccurs': '0', 'type': 'long'}, 'hasDependency': {'native': True, 'name': 'hasdependency', 'minOccurs': '0', 'type': 'boolean'}, 'progress': {'native': True, 'name': 'progress', 'minOccurs': '0', 'type': 'int'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}, 'parentTask': {'native': False, 'name': 'parenttask', 'minOccurs': '0', 'type': 'Link'}, 'completedTime': {'native': True, 'name': 'completedtime', 'minOccurs': '0', 'type': 'dateTime'}, 'pausedWorkItemId': {'native': True, 'name': 'pausedworkitemid', 'minOccurs': '0', 'type': 'long'}, 'currentNodeName': {'native': True, 'name': 'currentnodename', 'minOccurs': '0', 'type': 'string'}})
        self.cancellable = cancellable
        self.pausedtime = pausedtime
        self.user = user
        self.status = status
        self.type = type
        self.errormessage = errormessage
        self.workitemid = workitemid
        self.paused = paused
        self.result = result
        self.name = name
        self.proxyuser = proxyuser
        self.cancelled = cancelled
        self.completed = completed
        self.startedtime = startedtime
        self.visible = visible
        self.currentnodeid = currentnodeid
        self.hasdependency = hasdependency
        self.progress = progress
        self.id = id
        self.parenttask = parenttask
        self.completedtime = completedtime
        self.pausedworkitemid = pausedworkitemid
        self.currentnodename = currentnodename 
