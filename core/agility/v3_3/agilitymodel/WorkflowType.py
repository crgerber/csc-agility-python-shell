from core.agility.v3_3.agilitymodel.base.WorkflowType import WorkflowTypeBase
from core.agility.v3_3.agilitymodel.actions.WorkflowType import WorkflowTypeActions

class WorkflowType(WorkflowTypeBase, WorkflowTypeActions):
    '''
    classdocs
    '''
    def __init__(self, name='', description='', id=None):
        '''
        Constructor
        @param name: name
        @type name: string
        @param description: description
        @type description: string
        @param id: id
        @type id: int
        '''
        WorkflowTypeBase.__init__(self, name=name, description=description, id=id)
