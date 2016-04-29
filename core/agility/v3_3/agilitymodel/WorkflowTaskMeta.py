from core.agility.v3_3.agilitymodel.base.WorkflowTaskMeta import WorkflowTaskMetaBase
from core.agility.v3_3.agilitymodel.actions.WorkflowTaskMeta import WorkflowTaskMetaActions

class WorkflowTaskMeta(WorkflowTaskMetaBase, WorkflowTaskMetaActions):
    '''
    classdocs
    '''
    def __init__(self, pathicon='', name='', icon='', description='', transitions=[]):
        '''
        Constructor
        @param pathicon: pathicon
        @type pathicon: string
        @param name: name
        @type name: string
        @param icon: icon
        @type icon: string
        @param description: description
        @type description: string
        @param transitions: transitions minOccurs=0 maxOccurs=unbounded
        @type transitions: Link
        '''
        WorkflowTaskMetaBase.__init__(self, pathicon=pathicon, name=name, icon=icon, description=description, transitions=transitions)
