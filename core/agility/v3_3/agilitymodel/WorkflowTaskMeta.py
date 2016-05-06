from core.agility.v3_3.agilitymodel.base.WorkflowTaskMeta import WorkflowTaskMetaBase
from core.agility.v3_3.agilitymodel.actions.WorkflowTaskMeta import WorkflowTaskMetaActions

class WorkflowTaskMeta(WorkflowTaskMetaBase, WorkflowTaskMetaActions):
    '''
    classdocs
    '''
    def __init__(self, pathicon='', icon='', transitions=[], name='', description=''):
        '''
        Constructor
        @param pathicon: pathicon
        @type pathicon: string
        @param icon: icon
        @type icon: string
        @param transitions: transitions minOccurs=0 maxOccurs=unbounded
        @type transitions: Link
        @param name: name
        @type name: string
        @param description: description
        @type description: string
        '''
        WorkflowTaskMetaBase.__init__(self, pathicon=pathicon, icon=icon, transitions=transitions, name=name, description=description)
