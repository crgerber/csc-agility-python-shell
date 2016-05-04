from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, statemeta=[], publishstates=[], expectedexecutionpath=[], taskmeta=[], workfloweventid=None, workflowversion=None, assettypeid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'stateMeta': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'statemeta', 'minOccurs': '0', 'native': False}, 'publishStates': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'publishstates', 'minOccurs': '0', 'native': True}, 'expectedExecutionPath': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'expectedexecutionpath', 'minOccurs': '0', 'native': True}, 'taskMeta': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'taskmeta', 'minOccurs': '0', 'native': False}, 'workflowEventId': {'type': 'int', 'name': 'workfloweventid', 'native': True}, 'workflowVersion': {'type': 'int', 'name': 'workflowversion', 'native': True}, 'assetTypeId': {'type': 'int', 'name': 'assettypeid', 'native': True}})
        self.statemeta = statemeta
        self.publishstates = publishstates
        self.expectedexecutionpath = expectedexecutionpath
        self.taskmeta = taskmeta
        self.workfloweventid = workfloweventid
        self.workflowversion = workflowversion
        self.assettypeid = assettypeid 
