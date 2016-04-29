from .base.WorkflowTask import WorkflowTaskBase
from .actions.WorkflowTask import WorkflowTaskActions

class WorkflowTask(WorkflowTaskBase, WorkflowTaskActions):
    '''
    classdocs
    '''
    def __init__(self, candidategroupids=[], displayname='', description='', workfloweventid=None, variables=[], comments=[], destinationlocation='', assignee='', asset=None, workflowversionid=None, candidateuserids=[], actions=[], formname='', sourcelocation='', id=None, name=''):
        '''
        Constructor
        @param candidategroupids: candidategroupids minOccurs=0 maxOccurs=unbounded
        @type candidategroupids: string
        @param displayname: displayname
        @type displayname: string
        @param description: description
        @type description: string
        @param workfloweventid: workfloweventid
        @type workfloweventid: int
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: Link
        @param comments: comments minOccurs=0 maxOccurs=unbounded
        @type comments: string
        @param destinationlocation: destinationlocation
        @type destinationlocation: string
        @param assignee: assignee
        @type assignee: string
        @param asset: asset
        @type asset: Link
        @param workflowversionid: workflowversionid
        @type workflowversionid: int
        @param candidateuserids: candidateuserids minOccurs=0 maxOccurs=unbounded
        @type candidateuserids: string
        @param actions: actions minOccurs=0 maxOccurs=unbounded
        @type actions: string
        @param formname: formname
        @type formname: string
        @param sourcelocation: sourcelocation
        @type sourcelocation: string
        @param id: id
        @type id: int
        @param name: name
        @type name: string
        '''
        WorkflowTaskBase.__init__(self, candidategroupids=candidategroupids, displayname=displayname, description=description, workfloweventid=workfloweventid, variables=variables, comments=comments, destinationlocation=destinationlocation, assignee=assignee, asset=asset, workflowversionid=workflowversionid, candidateuserids=candidateuserids, actions=actions, formname=formname, sourcelocation=sourcelocation, id=id, name=name)
