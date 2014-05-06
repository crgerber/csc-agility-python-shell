from core.agility.v3_0.agilitymodel.base.Tasklist import TasklistBase
from core.agility.v3_0.agilitymodel.actions.Tasklist import TasklistActions

class Tasklist(TasklistBase, TasklistActions):
    '''
    classdocs
    '''
    def __init__(self, task=[], name='', offset=None, totalcount=None, limit=None, parentid=None):
        '''
        Constructor
        @param task: task minOccurs=0 maxOccurs=unbounded
        @type task: Task
        @param name: name
        @type name: string
        @param offset: offset
        @type offset: int
        @param totalcount: totalcount
        @type totalcount: int
        @param limit: limit
        @type limit: int
        @param parentid: parentid
        @type parentid: int
        '''
        TasklistBase.__init__(self, task=task, name=name, offset=offset, totalcount=totalcount, limit=limit, parentid=parentid)
