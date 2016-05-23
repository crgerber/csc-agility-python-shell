from core.agility.v3_3.agilitymodel.base.WorkflowType import WorkflowTypeBase
from core.agility.v3_3.agilitymodel.actions.WorkflowType import WorkflowTypeActions

class WorkflowType(WorkflowTypeBase, WorkflowTypeActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, name='', description=''):
        '''
        Constructor
        @param id: id
        @type id: int
        @param name: name
        @type name: string
        @param description: description
        @type description: string
        '''
        WorkflowTypeBase.__init__(self, id=id, name=name, description=description)
