from core.agility.common.AgilityModelBase import AgilityModelBase


class WorkflowMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, stateMeta=list(), publishStates=list(), expectedExecutionPath=list(), taskMeta=list(), workflowEventId=None, workflowVersion=None, assetTypeId=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'stateMeta': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'stateMeta', 'minOccurs': '0', 'native': False}, 'publishStates': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'publishStates', 'minOccurs': '0', 'native': True}, 'expectedExecutionPath': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'expectedExecutionPath', 'minOccurs': '0', 'native': True}, 'taskMeta': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'taskMeta', 'minOccurs': '0', 'native': False}, 'workflowEventId': {'type': 'int', 'name': 'workflowEventId', 'native': True}, 'workflowVersion': {'type': 'int', 'name': 'workflowVersion', 'native': True}, 'assetTypeId': {'type': 'int', 'name': 'assetTypeId', 'native': True}})
        self.stateMeta = stateMeta
        self.publishStates = publishStates
        self.expectedExecutionPath = expectedExecutionPath
        self.taskMeta = taskMeta
        self.workflowEventId = workflowEventId
        self.workflowVersion = workflowVersion
        self.assetTypeId = assetTypeId 
