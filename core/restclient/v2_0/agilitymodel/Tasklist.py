from core.restclient.v2_0.agilitymodel.base.Tasklist import TasklistBase
from core.restclient.v2_0.agilitymodel.actions.Tasklist import TasklistActions

class Tasklist(TasklistBase, TasklistActions):
    '''
    classdocs
    '''
    def __init__(self, Task=list(), name='', offset=None, totalCount=None, limit=None, parentId=None):
        '''
        Constructor
        @param Task: Task minOccurs=0 maxOccurs=unbounded
        @type Task: Task
        @param name: name
        @type name: string
        @param offset: offset
        @type offset: int
        @param totalCount: totalCount
        @type totalCount: int
        @param limit: limit
        @type limit: int
        @param parentId: parentId
        @type parentId: int
        '''
        TasklistBase.__init__(self, Task=Task, name=name, offset=offset, totalCount=totalCount, limit=limit, parentId=parentId)
