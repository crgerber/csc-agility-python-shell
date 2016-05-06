from core.agility.v3_3.agilitymodel.base.WorkflowPolicyMeta import WorkflowPolicyMetaBase
from core.agility.v3_3.agilitymodel.actions.WorkflowPolicyMeta import WorkflowPolicyMetaActions

class WorkflowPolicyMeta(WorkflowPolicyMetaBase, WorkflowPolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        WorkflowPolicyMetaBase.__init__(self)
