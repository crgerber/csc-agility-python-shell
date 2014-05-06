from base.Task import TaskBase
from actions.Task import TaskActions

class Task(TaskBase, TaskActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, name=None, proxyuser=None, completed=None, errormessage=None, completedtime=None, hasdependency=None, startedtime=None, user=None, cancelled=False, progress=None, parenttask=None, type=None, id=None, result=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param name: name minOccurs=0
        @type name: string
        @param proxyuser: proxyuser minOccurs=0
        @type proxyuser: string
        @param completed: completed minOccurs=0
        @type completed: boolean
        @param errormessage: errormessage minOccurs=0
        @type errormessage: string
        @param completedtime: completedtime minOccurs=0
        @type completedtime: dateTime
        @param hasdependency: hasdependency minOccurs=0
        @type hasdependency: boolean
        @param startedtime: startedtime minOccurs=0
        @type startedtime: dateTime
        @param user: user minOccurs=0
        @type user: string
        @param cancelled: cancelled
        @type cancelled: boolean
        @param progress: progress minOccurs=0
        @type progress: int
        @param parenttask: parenttask minOccurs=0
        @type parenttask: Link
        @param type: type minOccurs=0
        @type type: string
        @param id: id minOccurs=0
        @type id: int
        @param result: result minOccurs=0
        @type result: Link
        '''
        TaskBase.__init__(self, status=status, name=name, proxyuser=proxyuser, completed=completed, errormessage=errormessage, completedtime=completedtime, hasdependency=hasdependency, startedtime=startedtime, user=user, cancelled=cancelled, progress=progress, parenttask=parenttask, type=type, id=id, result=result)
