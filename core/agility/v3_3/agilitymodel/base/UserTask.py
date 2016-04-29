from core.agility.common.AgilityModelBase import AgilityModelBase

class UserTaskBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, candidategroup=[], completed=None, workflowtype=None, destination=None, assignee='', id=None, comment=[], workflowtask=None, requested=None, description='', asset=None, name='', candidateuser=[], source=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'candidateGroup': {'maxOccurs': 'unbounded', 'native': True, 'name': 'candidategroup', 'minOccurs': '0', 'type': 'string'}, 'completed': {'native': True, 'name': 'completed', 'type': 'dateTime'}, 'workflowType': {'native': False, 'name': 'workflowtype', 'type': 'Link'}, 'destination': {'native': False, 'name': 'destination', 'type': 'Link'}, 'assignee': {'native': True, 'name': 'assignee', 'type': 'string'}, 'id': {'native': True, 'name': 'id', 'type': 'int'}, 'comment': {'maxOccurs': 'unbounded', 'native': True, 'name': 'comment', 'minOccurs': '0', 'type': 'string'}, 'workflowTask': {'native': False, 'name': 'workflowtask', 'type': 'Link'}, 'requested': {'native': True, 'name': 'requested', 'type': 'dateTime'}, 'description': {'native': True, 'name': 'description', 'type': 'string'}, 'asset': {'native': False, 'name': 'asset', 'type': 'Link'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'candidateUser': {'maxOccurs': 'unbounded', 'native': True, 'name': 'candidateuser', 'minOccurs': '0', 'type': 'string'}, 'source': {'native': False, 'name': 'source', 'type': 'Link'}})
        self.candidategroup = candidategroup
        self.completed = completed
        self.workflowtype = workflowtype
        self.destination = destination
        self.assignee = assignee
        self.id = id
        self.comment = comment
        self.workflowtask = workflowtask
        self.requested = requested
        self.description = description
        self.asset = asset
        self.name = name
        self.candidateuser = candidateuser
        self.source = source 
