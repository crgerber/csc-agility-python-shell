from base.WorkflowTask import WorkflowTaskBase
from actions.WorkflowTask import WorkflowTaskActions

class WorkflowTask(WorkflowTaskBase, WorkflowTaskActions):
    '''
    classdocs
    '''
    def __init__(self, candidateGroupIds=list(), displayName='', description='', workflowEventId=None, variables=list(), comments=list(), destinationLocation='', assignee='', asset=None, workflowVersionId=None, candidateUserIds=list(), actions=list(), formName='', sourceLocation='', id=None, name=''):
        '''
        Constructor
        @param candidateGroupIds: candidateGroupIds minOccurs=0 maxOccurs=unbounded
        @type candidateGroupIds: string
        @param displayName: displayName
        @type displayName: string
        @param description: description
        @type description: string
        @param workflowEventId: workflowEventId
        @type workflowEventId: int
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: Link
        @param comments: comments minOccurs=0 maxOccurs=unbounded
        @type comments: string
        @param destinationLocation: destinationLocation
        @type destinationLocation: string
        @param assignee: assignee
        @type assignee: string
        @param asset: asset
        @type asset: Link
        @param workflowVersionId: workflowVersionId
        @type workflowVersionId: int
        @param candidateUserIds: candidateUserIds minOccurs=0 maxOccurs=unbounded
        @type candidateUserIds: string
        @param actions: actions minOccurs=0 maxOccurs=unbounded
        @type actions: string
        @param formName: formName
        @type formName: string
        @param sourceLocation: sourceLocation
        @type sourceLocation: string
        @param id: id
        @type id: int
        @param name: name
        @type name: string
        '''
        WorkflowTaskBase.__init__(self, candidateGroupIds=candidateGroupIds, displayName=displayName, description=description, workflowEventId=workflowEventId, variables=variables, comments=comments, destinationLocation=destinationLocation, assignee=assignee, asset=asset, workflowVersionId=workflowVersionId, candidateUserIds=candidateUserIds, actions=actions, formName=formName, sourceLocation=sourceLocation, id=id, name=name)
