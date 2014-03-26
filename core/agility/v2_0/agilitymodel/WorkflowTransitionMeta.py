from core.agility.v2_0.agilitymodel.base.WorkflowTransitionMeta import WorkflowTransitionMetaBase
from core.agility.v2_0.agilitymodel.actions.WorkflowTransitionMeta import WorkflowTransitionMetaActions

class WorkflowTransitionMeta(WorkflowTransitionMetaBase, WorkflowTransitionMetaActions):
    '''
    classdocs
    '''
    def __init__(self, name='', skipValidation=False, formName=''):
        '''
        Constructor
        @param name: name
        @type name: string
        @param skipValidation: skipValidation
        @type skipValidation: boolean
        @param formName: formName
        @type formName: string
        '''
        WorkflowTransitionMetaBase.__init__(self, name=name, skipValidation=skipValidation, formName=formName)
