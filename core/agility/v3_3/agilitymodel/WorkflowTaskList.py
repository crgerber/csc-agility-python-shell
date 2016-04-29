from core.agility.v3_3.agilitymodel.base.WorkflowTaskList import WorkflowTaskListBase
from core.agility.v3_3.agilitymodel.actions.WorkflowTaskList import WorkflowTaskListActions

class WorkflowTaskList(WorkflowTaskListBase, WorkflowTaskListActions):
    '''
    classdocs
    '''
    def __init__(self, tasks=[], totalcount=None):
        '''
        Constructor
        @param tasks: tasks minOccurs=0 maxOccurs=unbounded
        @type tasks: Link
        @param totalcount: totalcount
        @type totalcount: int
        '''
        WorkflowTaskListBase.__init__(self, tasks=tasks, totalcount=totalcount)
