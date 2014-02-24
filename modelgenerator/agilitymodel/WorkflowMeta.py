from base.WorkflowMeta import WorkflowMetaBase
from actions.WorkflowMeta import WorkflowMetaActions

class WorkflowMeta(WorkflowMetaBase, WorkflowMetaActions):
    '''
    classdocs
    '''
    def __init__(self, stateMeta=list(), publishStates=list(), expectedExecutionPath=list(), taskMeta=list(), workflowEventId=None, workflowVersion=None, assetTypeId=None):
        '''
        Constructor
        @param stateMeta: stateMeta minOccurs=0 maxOccurs=unbounded
        @type stateMeta: Link
        @param publishStates: publishStates minOccurs=0 maxOccurs=unbounded
        @type publishStates: string
        @param expectedExecutionPath: expectedExecutionPath minOccurs=0 maxOccurs=unbounded
        @type expectedExecutionPath: string
        @param taskMeta: taskMeta minOccurs=0 maxOccurs=unbounded
        @type taskMeta: Link
        @param workflowEventId: workflowEventId
        @type workflowEventId: int
        @param workflowVersion: workflowVersion
        @type workflowVersion: int
        @param assetTypeId: assetTypeId
        @type assetTypeId: int
        '''
        WorkflowMetaBase.__init__(self, stateMeta=stateMeta, publishStates=publishStates, expectedExecutionPath=expectedExecutionPath, taskMeta=taskMeta, workflowEventId=workflowEventId, workflowVersion=workflowVersion, assetTypeId=assetTypeId)
