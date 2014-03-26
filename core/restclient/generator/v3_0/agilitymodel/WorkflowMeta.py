from base.WorkflowMeta import WorkflowMetaBase
from actions.WorkflowMeta import WorkflowMetaActions

class WorkflowMeta(WorkflowMetaBase, WorkflowMetaActions):
    '''
    classdocs
    '''
    def __init__(self, statemeta=[], publishstates=[], expectedexecutionpath=[], taskmeta=[], workfloweventid=None, workflowversion=None, assettypeid=None):
        '''
        Constructor
        @param statemeta: statemeta minOccurs=0 maxOccurs=unbounded
        @type statemeta: Link
        @param publishstates: publishstates minOccurs=0 maxOccurs=unbounded
        @type publishstates: string
        @param expectedexecutionpath: expectedexecutionpath minOccurs=0 maxOccurs=unbounded
        @type expectedexecutionpath: string
        @param taskmeta: taskmeta minOccurs=0 maxOccurs=unbounded
        @type taskmeta: Link
        @param workfloweventid: workfloweventid
        @type workfloweventid: int
        @param workflowversion: workflowversion
        @type workflowversion: int
        @param assettypeid: assettypeid
        @type assettypeid: int
        '''
        WorkflowMetaBase.__init__(self, statemeta=statemeta, publishstates=publishstates, expectedexecutionpath=expectedexecutionpath, taskmeta=taskmeta, workfloweventid=workfloweventid, workflowversion=workflowversion, assettypeid=assettypeid)
