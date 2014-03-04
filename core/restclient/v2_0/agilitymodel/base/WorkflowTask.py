from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class WorkflowTaskBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, candidateGroupIds=list(), displayName='', description='', workflowEventId=None, variables=list(), comments=list(), destinationLocation='', assignee='', asset=None, workflowVersionId=None, candidateUserIds=list(), actions=list(), formName='', sourceLocation='', id=None, name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayName', 'native': True}, 'description': {'type': 'string', 'name': 'description', 'native': True}, 'assignee': {'type': 'string', 'name': 'assignee', 'native': True}, 'variables': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'candidateGroupIds': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'candidateGroupIds', 'minOccurs': '0', 'native': True}, 'comments': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'comments', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'workflowEventId': {'type': 'int', 'name': 'workflowEventId', 'native': True}, 'destinationLocation': {'type': 'string', 'name': 'destinationLocation', 'native': True}, 'workflowVersionId': {'type': 'int', 'name': 'workflowVersionId', 'native': True}, 'candidateUserIds': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'candidateUserIds', 'minOccurs': '0', 'native': True}, 'actions': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'actions', 'minOccurs': '0', 'native': True}, 'formName': {'type': 'string', 'name': 'formName', 'native': True}, 'sourceLocation': {'type': 'string', 'name': 'sourceLocation', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'asset': {'type': 'Link', 'name': 'asset', 'native': False}})
        self.candidateGroupIds = candidateGroupIds
        self.displayName = displayName
        self.description = description
        self.workflowEventId = workflowEventId
        self.variables = variables
        self.comments = comments
        self.destinationLocation = destinationLocation
        self.assignee = assignee
        self.asset = asset
        self.workflowVersionId = workflowVersionId
        self.candidateUserIds = candidateUserIds
        self.actions = actions
        self.formName = formName
        self.sourceLocation = sourceLocation
        self.id = id
        self.name = name 
