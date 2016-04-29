from core.agility.common.AgilityModelBase import AgilityModelBase

class WorkflowTaskBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, sourcelocation='', candidategroupids=[], formname='', description='', assignee='', destinationlocation='', displayname='', candidateuserids=[], id=None, asset=None, comments=[], workfloweventid=None, workflowversionid=None, name='', actions=[], variables=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'sourceLocation': {'native': True, 'name': 'sourcelocation', 'type': 'string'}, 'candidateGroupIds': {'maxOccurs': 'unbounded', 'native': True, 'name': 'candidategroupids', 'minOccurs': '0', 'type': 'string'}, 'formName': {'native': True, 'name': 'formname', 'type': 'string'}, 'workflowEventId': {'native': True, 'name': 'workfloweventid', 'type': 'int'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'assignee': {'native': True, 'name': 'assignee', 'type': 'string'}, 'variables': {'maxOccurs': 'unbounded', 'native': False, 'name': 'variables', 'minOccurs': '0', 'type': 'Link'}, 'destinationLocation': {'native': True, 'name': 'destinationlocation', 'type': 'string'}, 'displayName': {'native': True, 'name': 'displayname', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'workflowVersionId': {'native': True, 'name': 'workflowversionid', 'type': 'int'}, 'description': {'native': True, 'name': 'description', 'type': 'string'}, 'asset': {'native': False, 'name': 'asset', 'type': 'Link'}, 'candidateUserIds': {'maxOccurs': 'unbounded', 'native': True, 'name': 'candidateuserids', 'minOccurs': '0', 'type': 'string'}, 'actions': {'maxOccurs': 'unbounded', 'native': True, 'name': 'actions', 'minOccurs': '0', 'type': 'string'}, 'comments': {'maxOccurs': 'unbounded', 'native': True, 'name': 'comments', 'minOccurs': '0', 'type': 'string'}})
        self.sourcelocation = sourcelocation
        self.candidategroupids = candidategroupids
        self.formname = formname
        self.description = description
        self.assignee = assignee
        self.destinationlocation = destinationlocation
        self.displayname = displayname
        self.candidateuserids = candidateuserids
        self.id = id
        self.asset = asset
        self.comments = comments
        self.workfloweventid = workfloweventid
        self.workflowversionid = workflowversionid
        self.name = name
        self.actions = actions
        self.variables = variables 
