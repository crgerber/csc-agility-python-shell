from base.WorkflowPolicyMeta import WorkflowPolicyMetaBase
from actions.WorkflowPolicyMeta import WorkflowPolicyMetaActions

class WorkflowPolicyMeta(WorkflowPolicyMetaBase, WorkflowPolicyMetaActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        WorkflowPolicyMetaBase.__init__(self)
