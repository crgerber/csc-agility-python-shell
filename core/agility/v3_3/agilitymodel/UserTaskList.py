from core.agility.v3_3.agilitymodel.base.UserTaskList import UserTaskListBase
from core.agility.v3_3.agilitymodel.actions.UserTaskList import UserTaskListActions

class UserTaskList(UserTaskListBase, UserTaskListActions):
    '''
    classdocs
    '''
    def __init__(self, tasks=[], totalcount=None):
        '''
        Constructor
        @param tasks: tasks minOccurs=0 maxOccurs=unbounded
        @type tasks: UserTask
        @param totalcount: totalcount
        @type totalcount: int
        '''
        UserTaskListBase.__init__(self, tasks=tasks, totalcount=totalcount)
