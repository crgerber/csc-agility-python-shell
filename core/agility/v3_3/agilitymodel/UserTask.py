from base.UserTask import UserTaskBase
from actions.UserTask import UserTaskActions

class UserTask(UserTaskBase, UserTaskActions):
    '''
    classdocs
    '''
    def __init__(self, comment=[], requested=None, candidategroup=[], candidateuser=[], description='', assignee='', completed=None, destination=None, source=None, asset=None, workflowtask=None, workflowtype=None, id=None, name=''):
        '''
        Constructor
        @param comment: comment minOccurs=0 maxOccurs=unbounded
        @type comment: string
        @param requested: requested
        @type requested: dateTime
        @param candidategroup: candidategroup minOccurs=0 maxOccurs=unbounded
        @type candidategroup: string
        @param candidateuser: candidateuser minOccurs=0 maxOccurs=unbounded
        @type candidateuser: string
        @param description: description
        @type description: string
        @param assignee: assignee
        @type assignee: string
        @param completed: completed
        @type completed: dateTime
        @param destination: destination
        @type destination: Link
        @param source: source
        @type source: Link
        @param asset: asset
        @type asset: Link
        @param workflowtask: workflowtask
        @type workflowtask: Link
        @param workflowtype: workflowtype
        @type workflowtype: Link
        @param id: id
        @type id: int
        @param name: name
        @type name: string
        '''
        UserTaskBase.__init__(self, comment=comment, requested=requested, candidategroup=candidategroup, candidateuser=candidateuser, description=description, assignee=assignee, completed=completed, destination=destination, source=source, asset=asset, workflowtask=workflowtask, workflowtype=workflowtype, id=id, name=name)
