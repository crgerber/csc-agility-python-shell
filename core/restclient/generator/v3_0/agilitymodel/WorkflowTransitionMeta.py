from base.WorkflowTransitionMeta import WorkflowTransitionMetaBase
from actions.WorkflowTransitionMeta import WorkflowTransitionMetaActions

class WorkflowTransitionMeta(WorkflowTransitionMetaBase, WorkflowTransitionMetaActions):
    '''
    classdocs
    '''
    def __init__(self, name='', skipvalidation=False, formname=''):
        '''
        Constructor
        @param name: name
        @type name: string
        @param skipvalidation: skipvalidation
        @type skipvalidation: boolean
        @param formname: formname
        @type formname: string
        '''
        WorkflowTransitionMetaBase.__init__(self, name=name, skipvalidation=skipvalidation, formname=formname)
