from core.agility.common.AgilityModelBase import AgilityModelBase

class UserTaskBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, requested=None, workflowtype=None, assignee='', name='', candidategroup=[], workflowtask=None, id=None, candidateuser=[], description='', destination=None, completed=None, asset=None, source=None, comment=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'asset': {'name': 'asset', 'native': False, 'type': 'Link'}, 'requested': {'name': 'requested', 'native': True, 'type': 'dateTime'}, 'workflowType': {'name': 'workflowtype', 'native': False, 'type': 'Link'}, 'description': {'name': 'description', 'native': True, 'type': 'string'}, 'name': {'name': 'name', 'native': True, 'type': 'string'}, 'candidateGroup': {'name': 'candidategroup', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'workflowTask': {'name': 'workflowtask', 'native': False, 'type': 'Link'}, 'candidateUser': {'name': 'candidateuser', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'assignee': {'name': 'assignee', 'native': True, 'type': 'string'}, 'destination': {'name': 'destination', 'native': False, 'type': 'Link'}, 'completed': {'name': 'completed', 'native': True, 'type': 'dateTime'}, 'id': {'name': 'id', 'native': True, 'type': 'int'}, 'source': {'name': 'source', 'native': False, 'type': 'Link'}, 'comment': {'name': 'comment', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}})
        self.requested = requested
        self.workflowtype = workflowtype
        self.assignee = assignee
        self.name = name
        self.candidategroup = candidategroup
        self.workflowtask = workflowtask
        self.id = id
        self.candidateuser = candidateuser
        self.description = description
        self.destination = destination
        self.completed = completed
        self.asset = asset
        self.source = source
        self.comment = comment 
