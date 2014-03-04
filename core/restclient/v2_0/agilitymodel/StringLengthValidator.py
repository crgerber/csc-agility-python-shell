from core.restclient.v2_0.agilitymodel.base.StringLengthValidator import StringLengthValidatorBase
from core.restclient.v2_0.agilitymodel.actions.StringLengthValidator import StringLengthValidatorActions

class StringLengthValidator(StringLengthValidatorBase, StringLengthValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, minLength=None, maxLength=None):
        '''
        Constructor
        @param minLength: minLength minOccurs=0
        @type minLength: int
        @param maxLength: maxLength minOccurs=0
        @type maxLength: int
        '''
        StringLengthValidatorBase.__init__(self, minLength=minLength, maxLength=maxLength)
