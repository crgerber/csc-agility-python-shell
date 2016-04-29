from .base.WorkflowTaskList import WorkflowTaskListBase
from .actions.WorkflowTaskList import WorkflowTaskListActions

class WorkflowTaskList(WorkflowTaskListBase, WorkflowTaskListActions):
    '''
    classdocs
    '''
    def __init__(self, totalcount=None, tasks=[]):
        '''
        Constructor
        @param totalcount: totalcount
        @type totalcount: int
        @param tasks: tasks minOccurs=0 maxOccurs=unbounded
        @type tasks: Link
        '''
        WorkflowTaskListBase.__init__(self, totalcount=totalcount, tasks=tasks)
