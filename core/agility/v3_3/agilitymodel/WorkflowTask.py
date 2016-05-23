from core.agility.v3_3.agilitymodel.base.WorkflowTask import WorkflowTaskBase
from core.agility.v3_3.agilitymodel.actions.WorkflowTask import WorkflowTaskActions

class WorkflowTask(WorkflowTaskBase, WorkflowTaskActions):
    '''
    classdocs
    '''
    def __init__(self, comments=[], displayname='', formname='', assignee='', name='', sourcelocation='', actions=[], id=None, description='', variables=[], destinationlocation='', candidateuserids=[], asset=None, candidategroupids=[], workfloweventid=None, workflowversionid=None):
        '''
        Constructor
        @param comments: comments minOccurs=0 maxOccurs=unbounded
        @type comments: string
        @param displayname: displayname
        @type displayname: string
        @param formname: formname
        @type formname: string
        @param assignee: assignee
        @type assignee: string
        @param name: name
        @type name: string
        @param sourcelocation: sourcelocation
        @type sourcelocation: string
        @param actions: actions minOccurs=0 maxOccurs=unbounded
        @type actions: string
        @param id: id
        @type id: int
        @param description: description
        @type description: string
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: Link
        @param destinationlocation: destinationlocation
        @type destinationlocation: string
        @param candidateuserids: candidateuserids minOccurs=0 maxOccurs=unbounded
        @type candidateuserids: string
        @param asset: asset
        @type asset: Link
        @param candidategroupids: candidategroupids minOccurs=0 maxOccurs=unbounded
        @type candidategroupids: string
        @param workfloweventid: workfloweventid
        @type workfloweventid: int
        @param workflowversionid: workflowversionid
        @type workflowversionid: int
        '''
        WorkflowTaskBase.__init__(self, comments=comments, displayname=displayname, formname=formname, assignee=assignee, name=name, sourcelocation=sourcelocation, actions=actions, id=id, description=description, variables=variables, destinationlocation=destinationlocation, candidateuserids=candidateuserids, asset=asset, candidategroupids=candidategroupids, workfloweventid=workfloweventid, workflowversionid=workflowversionid)
