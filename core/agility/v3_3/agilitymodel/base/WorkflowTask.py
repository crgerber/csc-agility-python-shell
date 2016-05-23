from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowTaskBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, comments=[], displayname='', formname='', assignee='', name='', sourcelocation='', actions=[], id=None, description='', variables=[], destinationlocation='', candidateuserids=[], asset=None, candidategroupids=[], workfloweventid=None, workflowversionid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'comments': {'name': 'comments', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'asset': {'name': 'asset', 'native': False, 'type': 'Link'}, 'displayName': {'name': 'displayname', 'native': True, 'type': 'string'}, 'formName': {'name': 'formname', 'native': True, 'type': 'string'}, 'actions': {'name': 'actions', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'sourceLocation': {'name': 'sourcelocation', 'native': True, 'type': 'string'}, 'assignee': {'name': 'assignee', 'native': True, 'type': 'string'}, 'variables': {'name': 'variables', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'description': {'name': 'description', 'native': True, 'type': 'string'}, 'candidateUserIds': {'name': 'candidateuserids', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'id': {'name': 'id', 'native': True, 'type': 'int'}, 'candidateGroupIds': {'name': 'candidategroupids', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'workflowEventId': {'name': 'workfloweventid', 'native': True, 'type': 'int'}, 'workflowVersionId': {'name': 'workflowversionid', 'native': True, 'type': 'int'}, 'destinationLocation': {'name': 'destinationlocation', 'native': True, 'type': 'string'}})
        self.comments = comments
        self.displayname = displayname
        self.formname = formname
        self.assignee = assignee
        self.name = name
        self.sourcelocation = sourcelocation
        self.actions = actions
        self.id = id
        self.description = description
        self.variables = variables
        self.destinationlocation = destinationlocation
        self.candidateuserids = candidateuserids
        self.asset = asset
        self.candidategroupids = candidategroupids
        self.workfloweventid = workfloweventid
        self.workflowversionid = workflowversionid 
