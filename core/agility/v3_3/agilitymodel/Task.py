from core.agility.v3_3.agilitymodel.base.Task import TaskBase
from core.agility.v3_3.agilitymodel.actions.Task import TaskActions

class Task(TaskBase, TaskActions):
    '''
    classdocs
    '''
    def __init__(self, cancellable=None, pausedtime=None, user=None, status=None, type=None, errormessage=None, workitemid=None, paused=None, result=None, name=None, proxyuser=None, cancelled=False, completed=None, startedtime=None, visible=False, currentnodeid=None, hasdependency=None, progress=None, id=None, parenttask=None, completedtime=None, pausedworkitemid=None, currentnodename=None):
        '''
        Constructor
        @param cancellable: cancellable minOccurs=0
        @type cancellable: boolean
        @param pausedtime: pausedtime minOccurs=0
        @type pausedtime: dateTime
        @param user: user minOccurs=0
        @type user: string
        @param status: status minOccurs=0
        @type status: string
        @param type: type minOccurs=0
        @type type: string
        @param errormessage: errormessage minOccurs=0
        @type errormessage: string
        @param workitemid: workitemid minOccurs=0
        @type workitemid: long
        @param paused: paused minOccurs=0
        @type paused: boolean
        @param result: result minOccurs=0
        @type result: Link
        @param name: name minOccurs=0
        @type name: string
        @param proxyuser: proxyuser minOccurs=0
        @type proxyuser: string
        @param cancelled: cancelled
        @type cancelled: boolean
        @param completed: completed minOccurs=0
        @type completed: boolean
        @param startedtime: startedtime minOccurs=0
        @type startedtime: dateTime
        @param visible: visible
        @type visible: boolean
        @param currentnodeid: currentnodeid minOccurs=0
        @type currentnodeid: long
        @param hasdependency: hasdependency minOccurs=0
        @type hasdependency: boolean
        @param progress: progress minOccurs=0
        @type progress: int
        @param id: id minOccurs=0
        @type id: int
        @param parenttask: parenttask minOccurs=0
        @type parenttask: Link
        @param completedtime: completedtime minOccurs=0
        @type completedtime: dateTime
        @param pausedworkitemid: pausedworkitemid minOccurs=0
        @type pausedworkitemid: long
        @param currentnodename: currentnodename minOccurs=0
        @type currentnodename: string
        '''
        TaskBase.__init__(self, cancellable=cancellable, pausedtime=pausedtime, user=user, status=status, type=type, errormessage=errormessage, workitemid=workitemid, paused=paused, result=result, name=name, proxyuser=proxyuser, cancelled=cancelled, completed=completed, startedtime=startedtime, visible=visible, currentnodeid=currentnodeid, hasdependency=hasdependency, progress=progress, id=id, parenttask=parenttask, completedtime=completedtime, pausedworkitemid=pausedworkitemid, currentnodename=currentnodename)
