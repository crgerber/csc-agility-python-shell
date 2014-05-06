from core.agility.v3_0.agilitymodel.base.EmailValidator import EmailValidatorBase
from core.agility.v3_0.agilitymodel.actions.EmailValidator import EmailValidatorActions

class EmailValidator(EmailValidatorBase, EmailValidatorActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        EmailValidatorBase.__init__(self)
