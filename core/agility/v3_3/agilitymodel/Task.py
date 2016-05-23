from core.agility.v3_3.agilitymodel.base.Task import TaskBase
from core.agility.v3_3.agilitymodel.actions.Task import TaskActions

class Task(TaskBase, TaskActions):
    '''
    classdocs
    '''
    def __init__(self, workitemid=None, paused=None, type=None, parenttask=None, completed=None, status=None, id=None, user=None, progress=None, cancellable=None, startedtime=None, cancelled=False, completedtime=None, pausedtime=None, name=None, pausedworkitemid=None, result=None, currentnodeid=None, currentnodename=None, visible=False, hasdependency=None, proxyuser=None, errormessage=None):
        '''
        Constructor
        @param workitemid: workitemid minOccurs=0
        @type workitemid: long
        @param paused: paused minOccurs=0
        @type paused: boolean
        @param type: type minOccurs=0
        @type type: string
        @param parenttask: parenttask minOccurs=0
        @type parenttask: Link
        @param completed: completed minOccurs=0
        @type completed: boolean
        @param status: status minOccurs=0
        @type status: string
        @param id: id minOccurs=0
        @type id: int
        @param user: user minOccurs=0
        @type user: string
        @param progress: progress minOccurs=0
        @type progress: int
        @param cancellable: cancellable minOccurs=0
        @type cancellable: boolean
        @param startedtime: startedtime minOccurs=0
        @type startedtime: dateTime
        @param cancelled: cancelled
        @type cancelled: boolean
        @param completedtime: completedtime minOccurs=0
        @type completedtime: dateTime
        @param pausedtime: pausedtime minOccurs=0
        @type pausedtime: dateTime
        @param name: name minOccurs=0
        @type name: string
        @param pausedworkitemid: pausedworkitemid minOccurs=0
        @type pausedworkitemid: long
        @param result: result minOccurs=0
        @type result: Link
        @param currentnodeid: currentnodeid minOccurs=0
        @type currentnodeid: long
        @param currentnodename: currentnodename minOccurs=0
        @type currentnodename: string
        @param visible: visible
        @type visible: boolean
        @param hasdependency: hasdependency minOccurs=0
        @type hasdependency: boolean
        @param proxyuser: proxyuser minOccurs=0
        @type proxyuser: string
        @param errormessage: errormessage minOccurs=0
        @type errormessage: string
        '''
        TaskBase.__init__(self, workitemid=workitemid, paused=paused, type=type, parenttask=parenttask, completed=completed, status=status, id=id, user=user, progress=progress, cancellable=cancellable, startedtime=startedtime, cancelled=cancelled, completedtime=completedtime, pausedtime=pausedtime, name=name, pausedworkitemid=pausedworkitemid, result=result, currentnodeid=currentnodeid, currentnodename=currentnodename, visible=visible, hasdependency=hasdependency, proxyuser=proxyuser, errormessage=errormessage)
