from core.agility.v3_3.agilitymodel.base.Task import TaskBase
from core.agility.v3_3.agilitymodel.actions.Task import TaskActions

class Task(TaskBase, TaskActions):
    '''
    classdocs
    '''
    def __init__(self, workitemid=None, parenttask=None, paused=None, visible=False, result=None, id=None, pausedworkitemid=None, completedtime=None, startedtime=None, progress=None, type=None, status=None, completed=None, errormessage=None, hasdependency=None, user=None, currentnodeid=None, name=None, proxyuser=None, cancellable=None, pausedtime=None, cancelled=False, currentnodename=None):
        '''
        Constructor
        @param workitemid: workitemid minOccurs=0
        @type workitemid: long
        @param parenttask: parenttask minOccurs=0
        @type parenttask: Link
        @param paused: paused minOccurs=0
        @type paused: boolean
        @param visible: visible
        @type visible: boolean
        @param result: result minOccurs=0
        @type result: Link
        @param id: id minOccurs=0
        @type id: int
        @param pausedworkitemid: pausedworkitemid minOccurs=0
        @type pausedworkitemid: long
        @param completedtime: completedtime minOccurs=0
        @type completedtime: dateTime
        @param startedtime: startedtime minOccurs=0
        @type startedtime: dateTime
        @param progress: progress minOccurs=0
        @type progress: int
        @param type: type minOccurs=0
        @type type: string
        @param status: status minOccurs=0
        @type status: string
        @param completed: completed minOccurs=0
        @type completed: boolean
        @param errormessage: errormessage minOccurs=0
        @type errormessage: string
        @param hasdependency: hasdependency minOccurs=0
        @type hasdependency: boolean
        @param user: user minOccurs=0
        @type user: string
        @param currentnodeid: currentnodeid minOccurs=0
        @type currentnodeid: long
        @param name: name minOccurs=0
        @type name: string
        @param proxyuser: proxyuser minOccurs=0
        @type proxyuser: string
        @param cancellable: cancellable minOccurs=0
        @type cancellable: boolean
        @param pausedtime: pausedtime minOccurs=0
        @type pausedtime: dateTime
        @param cancelled: cancelled
        @type cancelled: boolean
        @param currentnodename: currentnodename minOccurs=0
        @type currentnodename: string
        '''
        TaskBase.__init__(self, workitemid=workitemid, parenttask=parenttask, paused=paused, visible=visible, result=result, id=id, pausedworkitemid=pausedworkitemid, completedtime=completedtime, startedtime=startedtime, progress=progress, type=type, status=status, completed=completed, errormessage=errormessage, hasdependency=hasdependency, user=user, currentnodeid=currentnodeid, name=name, proxyuser=proxyuser, cancellable=cancellable, pausedtime=pausedtime, cancelled=cancelled, currentnodename=currentnodename)
