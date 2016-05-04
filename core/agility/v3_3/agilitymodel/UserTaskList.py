from core.agility.v3_3.agilitymodel.base.UserTaskList import UserTaskListBase
from core.agility.v3_3.agilitymodel.actions.UserTaskList import UserTaskListActions

class UserTaskList(UserTaskListBase, UserTaskListActions):
    '''
    classdocs
    '''
    def __init__(self, totalcount=None, tasks=[]):
        '''
        Constructor
        @param totalcount: totalcount
        @type totalcount: int
        @param tasks: tasks minOccurs=0 maxOccurs=unbounded
        @type tasks: UserTask
        '''
        UserTaskListBase.__init__(self, totalcount=totalcount, tasks=tasks)
