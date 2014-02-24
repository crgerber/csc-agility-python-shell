from base.WorkflowTaskList import WorkflowTaskListBase
from actions.WorkflowTaskList import WorkflowTaskListActions

class WorkflowTaskList(WorkflowTaskListBase, WorkflowTaskListActions):
    '''
    classdocs
    '''
    def __init__(self, totalCount=None, tasks=list()):
        '''
        Constructor
        @param totalCount: totalCount
        @type totalCount: int
        @param tasks: tasks minOccurs=0 maxOccurs=unbounded
        @type tasks: Link
        '''
        WorkflowTaskListBase.__init__(self, totalCount=totalCount, tasks=tasks)
