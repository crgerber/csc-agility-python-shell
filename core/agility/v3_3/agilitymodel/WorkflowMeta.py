from core.agility.v3_3.agilitymodel.base.WorkflowMeta import WorkflowMetaBase
from core.agility.v3_3.agilitymodel.actions.WorkflowMeta import WorkflowMetaActions

class WorkflowMeta(WorkflowMetaBase, WorkflowMetaActions):
    '''
    classdocs
    '''
    def __init__(self, workflowversion=None, statemeta=[], assettypeid=None, taskmeta=[], expectedexecutionpath=[], workfloweventid=None, publishstates=[]):
        '''
        Constructor
        @param workflowversion: workflowversion
        @type workflowversion: int
        @param statemeta: statemeta minOccurs=0 maxOccurs=unbounded
        @type statemeta: Link
        @param assettypeid: assettypeid
        @type assettypeid: int
        @param taskmeta: taskmeta minOccurs=0 maxOccurs=unbounded
        @type taskmeta: Link
        @param expectedexecutionpath: expectedexecutionpath minOccurs=0 maxOccurs=unbounded
        @type expectedexecutionpath: string
        @param workfloweventid: workfloweventid
        @type workfloweventid: int
        @param publishstates: publishstates minOccurs=0 maxOccurs=unbounded
        @type publishstates: string
        '''
        WorkflowMetaBase.__init__(self, workflowversion=workflowversion, statemeta=statemeta, assettypeid=assettypeid, taskmeta=taskmeta, expectedexecutionpath=expectedexecutionpath, workfloweventid=workfloweventid, publishstates=publishstates)
