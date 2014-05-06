from core.agility.v3_0.agilitymodel.base.StringLengthValidator import StringLengthValidatorBase
from core.agility.v3_0.agilitymodel.actions.StringLengthValidator import StringLengthValidatorActions

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
