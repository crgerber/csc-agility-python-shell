from core.agility.v3_3.agilitymodel.base.UserTask import UserTaskBase
from core.agility.v3_3.agilitymodel.actions.UserTask import UserTaskActions

class UserTask(UserTaskBase, UserTaskActions):
    '''
    classdocs
    '''
    def __init__(self, requested=None, workflowtype=None, assignee='', name='', candidategroup=[], workflowtask=None, id=None, candidateuser=[], description='', destination=None, completed=None, asset=None, source=None, comment=[]):
        '''
        Constructor
        @param requested: requested
        @type requested: dateTime
        @param workflowtype: workflowtype
        @type workflowtype: Link
        @param assignee: assignee
        @type assignee: string
        @param name: name
        @type name: string
        @param candidategroup: candidategroup minOccurs=0 maxOccurs=unbounded
        @type candidategroup: string
        @param workflowtask: workflowtask
        @type workflowtask: Link
        @param id: id
        @type id: int
        @param candidateuser: candidateuser minOccurs=0 maxOccurs=unbounded
        @type candidateuser: string
        @param description: description
        @type description: string
        @param destination: destination
        @type destination: Link
        @param completed: completed
        @type completed: dateTime
        @param asset: asset
        @type asset: Link
        @param source: source
        @type source: Link
        @param comment: comment minOccurs=0 maxOccurs=unbounded
        @type comment: string
        '''
        UserTaskBase.__init__(self, requested=requested, workflowtype=workflowtype, assignee=assignee, name=name, candidategroup=candidategroup, workflowtask=workflowtask, id=id, candidateuser=candidateuser, description=description, destination=destination, completed=completed, asset=asset, source=source, comment=comment)
