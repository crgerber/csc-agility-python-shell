from core.agility.v3_3.agilitymodel.base.Tasklist import TasklistBase
from core.agility.v3_3.agilitymodel.actions.Tasklist import TasklistActions

class Tasklist(TasklistBase, TasklistActions):
    '''
    classdocs
    '''
    def __init__(self, limit=None, offset=None, name='', task=[], totalcount=None, parentid=None):
        '''
        Constructor
        @param limit: limit
        @type limit: int
        @param offset: offset
        @type offset: int
        @param name: name
        @type name: string
        @param task: task minOccurs=0 maxOccurs=unbounded
        @type task: Task
        @param totalcount: totalcount
        @type totalcount: int
        @param parentid: parentid
        @type parentid: int
        '''
        TasklistBase.__init__(self, limit=limit, offset=offset, name=name, task=task, totalcount=totalcount, parentid=parentid)
