from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, workflowversion=None, statemeta=[], assettypeid=None, taskmeta=[], expectedexecutionpath=[], workfloweventid=None, publishstates=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'workflowVersion': {'name': 'workflowversion', 'native': True, 'type': 'int'}, 'stateMeta': {'name': 'statemeta', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'assetTypeId': {'name': 'assettypeid', 'native': True, 'type': 'int'}, 'taskMeta': {'name': 'taskmeta', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'expectedExecutionPath': {'name': 'expectedexecutionpath', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'workflowEventId': {'name': 'workfloweventid', 'native': True, 'type': 'int'}, 'publishStates': {'name': 'publishstates', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}})
        self.workflowversion = workflowversion
        self.statemeta = statemeta
        self.assettypeid = assettypeid
        self.taskmeta = taskmeta
        self.expectedexecutionpath = expectedexecutionpath
        self.workfloweventid = workfloweventid
        self.publishstates = publishstates 
