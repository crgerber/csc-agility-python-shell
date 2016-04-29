from core.agility.v3_3.agilitymodel.base.WorkflowMeta import WorkflowMetaBase
from core.agility.v3_3.agilitymodel.actions.WorkflowMeta import WorkflowMetaActions

class WorkflowMeta(WorkflowMetaBase, WorkflowMetaActions):
    '''
    classdocs
    '''
    def __init__(self, statemeta=[], assettypeid=None, workfloweventid=None, publishstates=[], taskmeta=[], workflowversion=None, expectedexecutionpath=[]):
        '''
        Constructor
        @param statemeta: statemeta minOccurs=0 maxOccurs=unbounded
        @type statemeta: Link
        @param assettypeid: assettypeid
        @type assettypeid: int
        @param workfloweventid: workfloweventid
        @type workfloweventid: int
        @param publishstates: publishstates minOccurs=0 maxOccurs=unbounded
        @type publishstates: string
        @param taskmeta: taskmeta minOccurs=0 maxOccurs=unbounded
        @type taskmeta: Link
        @param workflowversion: workflowversion
        @type workflowversion: int
        @param expectedexecutionpath: expectedexecutionpath minOccurs=0 maxOccurs=unbounded
        @type expectedexecutionpath: string
        '''
        WorkflowMetaBase.__init__(self, statemeta=statemeta, assettypeid=assettypeid, workfloweventid=workfloweventid, publishstates=publishstates, taskmeta=taskmeta, workflowversion=workflowversion, expectedexecutionpath=expectedexecutionpath)
