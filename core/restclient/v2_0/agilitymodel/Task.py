from core.restclient.v2_0.agilitymodel.base.Task import TaskBase
from core.restclient.v2_0.agilitymodel.actions.Task import TaskActions

class Task(TaskBase, TaskActions):
    '''
    classdocs
    '''
    def __init__(self, status=None, name=None, proxyUser=None, completed=None, errorMessage=None, completedTime=None, hasDependency=None, startedTime=None, user=None, parentTask=None, progress=None, type=None, id=None, result=None):
        '''
        Constructor
        @param status: status minOccurs=0
        @type status: string
        @param name: name minOccurs=0
        @type name: string
        @param proxyUser: proxyUser minOccurs=0
        @type proxyUser: string
        @param completed: completed minOccurs=0
        @type completed: boolean
        @param errorMessage: errorMessage minOccurs=0
        @type errorMessage: string
        @param completedTime: completedTime minOccurs=0
        @type completedTime: dateTime
        @param hasDependency: hasDependency minOccurs=0
        @type hasDependency: boolean
        @param startedTime: startedTime minOccurs=0
        @type startedTime: dateTime
        @param user: user minOccurs=0
        @type user: string
        @param parentTask: parentTask minOccurs=0
        @type parentTask: Link
        @param progress: progress minOccurs=0
        @type progress: int
        @param type: type minOccurs=0
        @type type: string
        @param id: id minOccurs=0
        @type id: int
        @param result: result minOccurs=0
        @type result: Link
        '''
        TaskBase.__init__(self, status=status, name=name, proxyUser=proxyUser, completed=completed, errorMessage=errorMessage, completedTime=completedTime, hasDependency=hasDependency, startedTime=startedTime, user=user, parentTask=parentTask, progress=progress, type=type, id=id, result=result)
