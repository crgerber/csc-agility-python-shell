from base.WorkflowType import WorkflowTypeBase
from actions.WorkflowType import WorkflowTypeActions

class WorkflowType(WorkflowTypeBase, WorkflowTypeActions):
    '''
    classdocs
    '''
    def __init__(self, description='', id=None, name=''):
        '''
        Constructor
        @param description: description
        @type description: string
        @param id: id
        @type id: int
        @param name: name
        @type name: string
        '''
        WorkflowTypeBase.__init__(self, description=description, id=id, name=name)
