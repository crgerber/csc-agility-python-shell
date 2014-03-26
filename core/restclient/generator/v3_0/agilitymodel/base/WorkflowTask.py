from AgilityModelBase import AgilityModelBase

class WorkflowTaskBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, candidategroupids=[], displayname='', description='', workfloweventid=None, variables=[], comments=[], destinationlocation='', assignee='', asset=None, workflowversionid=None, candidateuserids=[], actions=[], formname='', sourcelocation='', id=None, name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayname', 'native': True}, 'description': {'type': 'string', 'name': 'description', 'native': True}, 'assignee': {'type': 'string', 'name': 'assignee', 'native': True}, 'variables': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'candidateGroupIds': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'candidategroupids', 'minOccurs': '0', 'native': True}, 'comments': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'comments', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'workflowEventId': {'type': 'int', 'name': 'workfloweventid', 'native': True}, 'destinationLocation': {'type': 'string', 'name': 'destinationlocation', 'native': True}, 'workflowVersionId': {'type': 'int', 'name': 'workflowversionid', 'native': True}, 'candidateUserIds': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'candidateuserids', 'minOccurs': '0', 'native': True}, 'actions': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'actions', 'minOccurs': '0', 'native': True}, 'formName': {'type': 'string', 'name': 'formname', 'native': True}, 'sourceLocation': {'type': 'string', 'name': 'sourcelocation', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'asset': {'type': 'Link', 'name': 'asset', 'native': False}})
        self.candidategroupids = candidategroupids
        self.displayname = displayname
        self.description = description
        self.workfloweventid = workfloweventid
        self.variables = variables
        self.comments = comments
        self.destinationlocation = destinationlocation
        self.assignee = assignee
        self.asset = asset
        self.workflowversionid = workflowversionid
        self.candidateuserids = candidateuserids
        self.actions = actions
        self.formname = formname
        self.sourcelocation = sourcelocation
        self.id = id
        self.name = name 
