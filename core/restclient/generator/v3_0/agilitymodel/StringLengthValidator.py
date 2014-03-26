from base.StringLengthValidator import StringLengthValidatorBase
from actions.StringLengthValidator import StringLengthValidatorActions

class StringLengthValidator(StringLengthValidatorBase, StringLengthValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, minlength=None, maxlength=None):
        '''
        Constructor
        @param minlength: minlength minOccurs=0
        @type minlength: int
        @param maxlength: maxlength minOccurs=0
        @type maxlength: int
        '''
        StringLengthValidatorBase.__init__(self, minlength=minlength, maxlength=maxlength)
