from core.agility.v3_3.agilitymodel.base.StringLengthValidator import StringLengthValidatorBase
from core.agility.v3_3.agilitymodel.actions.StringLengthValidator import StringLengthValidatorActions

class StringLengthValidator(StringLengthValidatorBase, StringLengthValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, maxlength=None, minlength=None):
        '''
        Constructor
        @param maxlength: maxlength minOccurs=0
        @type maxlength: int
        @param minlength: minlength minOccurs=0
        @type minlength: int
        '''
        StringLengthValidatorBase.__init__(self, maxlength=maxlength, minlength=minlength)
