from base.WorkflowTaskMeta import WorkflowTaskMetaBase
from actions.WorkflowTaskMeta import WorkflowTaskMetaActions

class WorkflowTaskMeta(WorkflowTaskMetaBase, WorkflowTaskMetaActions):
    '''
    classdocs
    '''
    def __init__(self, pathIcon='', icon='', transitions=list(), name='', description=''):
        '''
        Constructor
        @param pathIcon: pathIcon
        @type pathIcon: string
        @param icon: icon
        @type icon: string
        @param transitions: transitions minOccurs=0 maxOccurs=unbounded
        @type transitions: Link
        @param name: name
        @type name: string
        @param description: description
        @type description: string
        '''
        WorkflowTaskMetaBase.__init__(self, pathIcon=pathIcon, icon=icon, transitions=transitions, name=name, description=description)
