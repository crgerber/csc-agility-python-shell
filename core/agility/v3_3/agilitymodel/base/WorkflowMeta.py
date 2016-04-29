from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, statemeta=[], assettypeid=None, workfloweventid=None, publishstates=[], taskmeta=[], workflowversion=None, expectedexecutionpath=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'stateMeta': {'maxOccurs': 'unbounded', 'native': False, 'name': 'statemeta', 'minOccurs': '0', 'type': 'Link'}, 'assetTypeId': {'native': True, 'name': 'assettypeid', 'type': 'int'}, 'workflowEventId': {'native': True, 'name': 'workfloweventid', 'type': 'int'}, 'publishStates': {'maxOccurs': 'unbounded', 'native': True, 'name': 'publishstates', 'minOccurs': '0', 'type': 'string'}, 'taskMeta': {'maxOccurs': 'unbounded', 'native': False, 'name': 'taskmeta', 'minOccurs': '0', 'type': 'Link'}, 'workflowVersion': {'native': True, 'name': 'workflowversion', 'type': 'int'}, 'expectedExecutionPath': {'maxOccurs': 'unbounded', 'native': True, 'name': 'expectedexecutionpath', 'minOccurs': '0', 'type': 'string'}})
        self.statemeta = statemeta
        self.assettypeid = assettypeid
        self.workfloweventid = workfloweventid
        self.publishstates = publishstates
        self.taskmeta = taskmeta
        self.workflowversion = workflowversion
        self.expectedexecutionpath = expectedexecutionpath 
