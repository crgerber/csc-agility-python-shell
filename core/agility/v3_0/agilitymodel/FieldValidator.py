from core.agility.v3_0.agilitymodel.base.FieldValidator import FieldValidatorBase
from core.agility.v3_0.agilitymodel.actions.FieldValidator import FieldValidatorActions

class FieldValidator(FieldValidatorBase, FieldValidatorActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        FieldValidatorBase.__init__(self)
