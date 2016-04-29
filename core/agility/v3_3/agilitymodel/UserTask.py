from core.agility.v3_3.agilitymodel.base.UserTask import UserTaskBase
from core.agility.v3_3.agilitymodel.actions.UserTask import UserTaskActions

class UserTask(UserTaskBase, UserTaskActions):
    '''
    classdocs
    '''
    def __init__(self, candidategroup=[], completed=None, workflowtype=None, destination=None, assignee='', id=None, comment=[], workflowtask=None, requested=None, description='', asset=None, name='', candidateuser=[], source=None):
        '''
        Constructor
        @param candidategroup: candidategroup minOccurs=0 maxOccurs=unbounded
        @type candidategroup: string
        @param completed: completed
        @type completed: dateTime
        @param workflowtype: workflowtype
        @type workflowtype: Link
        @param destination: destination
        @type destination: Link
        @param assignee: assignee
        @type assignee: string
        @param id: id
        @type id: int
        @param comment: comment minOccurs=0 maxOccurs=unbounded
        @type comment: string
        @param workflowtask: workflowtask
        @type workflowtask: Link
        @param requested: requested
        @type requested: dateTime
        @param description: description
        @type description: string
        @param asset: asset
        @type asset: Link
        @param name: name
        @type name: string
        @param candidateuser: candidateuser minOccurs=0 maxOccurs=unbounded
        @type candidateuser: string
        @param source: source
        @type source: Link
        '''
        UserTaskBase.__init__(self, candidategroup=candidategroup, completed=completed, workflowtype=workflowtype, destination=destination, assignee=assignee, id=id, comment=comment, workflowtask=workflowtask, requested=requested, description=description, asset=asset, name=name, candidateuser=candidateuser, source=source)
