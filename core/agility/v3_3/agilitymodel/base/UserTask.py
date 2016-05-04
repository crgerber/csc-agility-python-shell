from core.agility.common.AgilityModelBase import AgilityModelBase

class UserTaskBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, comment=[], requested=None, candidategroup=[], candidateuser=[], description='', assignee='', completed=None, destination=None, source=None, asset=None, workflowtask=None, workflowtype=None, id=None, name=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'comment': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'comment', 'minOccurs': '0', 'native': True}, 'requested': {'type': 'dateTime', 'name': 'requested', 'native': True}, 'candidateGroup': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'candidategroup', 'minOccurs': '0', 'native': True}, 'candidateUser': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'candidateuser', 'minOccurs': '0', 'native': True}, 'description': {'type': 'string', 'name': 'description', 'native': True}, 'source': {'type': 'Link', 'name': 'source', 'native': False}, 'completed': {'type': 'dateTime', 'name': 'completed', 'native': True}, 'destination': {'type': 'Link', 'name': 'destination', 'native': False}, 'assignee': {'type': 'string', 'name': 'assignee', 'native': True}, 'asset': {'type': 'Link', 'name': 'asset', 'native': False}, 'workflowTask': {'type': 'Link', 'name': 'workflowtask', 'native': False}, 'workflowType': {'type': 'Link', 'name': 'workflowtype', 'native': False}, 'id': {'type': 'int', 'name': 'id', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}})
        self.comment = comment
        self.requested = requested
        self.candidategroup = candidategroup
        self.candidateuser = candidateuser
        self.description = description
        self.assignee = assignee
        self.completed = completed
        self.destination = destination
        self.source = source
        self.asset = asset
        self.workflowtask = workflowtask
        self.workflowtype = workflowtype
        self.id = id
        self.name = name 
