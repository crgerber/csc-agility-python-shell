from core.agility.v3_3.agilitymodel.base.WorkflowTransitionMeta import WorkflowTransitionMetaBase
from core.agility.v3_3.agilitymodel.actions.WorkflowTransitionMeta import WorkflowTransitionMetaActions

class WorkflowTransitionMeta(WorkflowTransitionMetaBase, WorkflowTransitionMetaActions):
    '''
    classdocs
    '''
    def __init__(self, skipvalidation=False, name='', formname=''):
        '''
        Constructor
        @param skipvalidation: skipvalidation
        @type skipvalidation: boolean
        @param name: name
        @type name: string
        @param formname: formname
        @type formname: string
        '''
        WorkflowTransitionMetaBase.__init__(self, skipvalidation=skipvalidation, name=name, formname=formname)
