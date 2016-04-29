from .base.WorkflowRequest import WorkflowRequestBase
from .actions.WorkflowRequest import WorkflowRequestActions

class WorkflowRequest(WorkflowRequestBase, WorkflowRequestActions):
    '''
    classdocs
    '''
    def __init__(self, comment=None):
        '''
        Constructor
        @param comment: comment minOccurs=0
        @type comment: string
        '''
        WorkflowRequestBase.__init__(self, comment=comment)
