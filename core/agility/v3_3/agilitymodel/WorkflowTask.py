from core.agility.v3_3.agilitymodel.base.WorkflowTask import WorkflowTaskBase
from core.agility.v3_3.agilitymodel.actions.WorkflowTask import WorkflowTaskActions

class WorkflowTask(WorkflowTaskBase, WorkflowTaskActions):
    '''
    classdocs
    '''
    def __init__(self, sourcelocation='', candidategroupids=[], formname='', description='', assignee='', destinationlocation='', displayname='', candidateuserids=[], id=None, asset=None, comments=[], workfloweventid=None, workflowversionid=None, name='', actions=[], variables=[]):
        '''
        Constructor
        @param sourcelocation: sourcelocation
        @type sourcelocation: string
        @param candidategroupids: candidategroupids minOccurs=0 maxOccurs=unbounded
        @type candidategroupids: string
        @param formname: formname
        @type formname: string
        @param description: description
        @type description: string
        @param assignee: assignee
        @type assignee: string
        @param destinationlocation: destinationlocation
        @type destinationlocation: string
        @param displayname: displayname
        @type displayname: string
        @param candidateuserids: candidateuserids minOccurs=0 maxOccurs=unbounded
        @type candidateuserids: string
        @param id: id
        @type id: int
        @param asset: asset
        @type asset: Link
        @param comments: comments minOccurs=0 maxOccurs=unbounded
        @type comments: string
        @param workfloweventid: workfloweventid
        @type workfloweventid: int
        @param workflowversionid: workflowversionid
        @type workflowversionid: int
        @param name: name
        @type name: string
        @param actions: actions minOccurs=0 maxOccurs=unbounded
        @type actions: string
        @param variables: variables minOccurs=0 maxOccurs=unbounded
        @type variables: Link
        '''
        WorkflowTaskBase.__init__(self, sourcelocation=sourcelocation, candidategroupids=candidategroupids, formname=formname, description=description, assignee=assignee, destinationlocation=destinationlocation, displayname=displayname, candidateuserids=candidateuserids, id=id, asset=asset, comments=comments, workfloweventid=workfloweventid, workflowversionid=workflowversionid, name=name, actions=actions, variables=variables)
