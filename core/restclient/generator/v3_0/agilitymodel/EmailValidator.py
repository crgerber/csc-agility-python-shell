from base.EmailValidator import EmailValidatorBase
from actions.EmailValidator import EmailValidatorActions

class EmailValidator(EmailValidatorBase, EmailValidatorActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        EmailValidatorBase.__init__(self)
