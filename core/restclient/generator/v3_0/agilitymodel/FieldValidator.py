from .base.FieldValidator import FieldValidatorBase
from .actions.FieldValidator import FieldValidatorActions

class FieldValidator(FieldValidatorBase, FieldValidatorActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        FieldValidatorBase.__init__(self)
