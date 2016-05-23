from core.agility.v3_3.agilitymodel.base.WorkflowTaskMeta import WorkflowTaskMetaBase
from core.agility.v3_3.agilitymodel.actions.WorkflowTaskMeta import WorkflowTaskMetaActions

class WorkflowTaskMeta(WorkflowTaskMetaBase, WorkflowTaskMetaActions):
    '''
    classdocs
    '''
    def __init__(self, name='', description='', transitions=[], pathicon='', icon=''):
        '''
        Constructor
        @param name: name
        @type name: string
        @param description: description
        @type description: string
        @param transitions: transitions minOccurs=0 maxOccurs=unbounded
        @type transitions: Link
        @param pathicon: pathicon
        @type pathicon: string
        @param icon: icon
        @type icon: string
        '''
        WorkflowTaskMetaBase.__init__(self, name=name, description=description, transitions=transitions, pathicon=pathicon, icon=icon)
