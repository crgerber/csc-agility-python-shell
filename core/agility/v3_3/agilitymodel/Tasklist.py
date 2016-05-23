from core.agility.v3_3.agilitymodel.base.Tasklist import TasklistBase
from core.agility.v3_3.agilitymodel.actions.Tasklist import TasklistActions

class Tasklist(TasklistBase, TasklistActions):
    '''
    classdocs
    '''
    def __init__(self, task=[], totalcount=None, parentid=None, name='', limit=None, offset=None):
        '''
        Constructor
        @param task: task minOccurs=0 maxOccurs=unbounded
        @type task: Task
        @param totalcount: totalcount
        @type totalcount: int
        @param parentid: parentid
        @type parentid: int
        @param name: name
        @type name: string
        @param limit: limit
        @type limit: int
        @param offset: offset
        @type offset: int
        '''
        TasklistBase.__init__(self, task=task, totalcount=totalcount, parentid=parentid, name=name, limit=limit, offset=offset)
