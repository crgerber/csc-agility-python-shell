from core.restclient.v2_0.agilitymodel.base.WorkflowRequest import WorkflowRequestBase
from core.restclient.v2_0.agilitymodel.actions.WorkflowRequest import WorkflowRequestActions

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
