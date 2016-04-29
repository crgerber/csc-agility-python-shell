from .base.RegexValidator import RegexValidatorBase
from .actions.RegexValidator import RegexValidatorActions

class RegexValidator(RegexValidatorBase, RegexValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, expression=[]):
        '''
        Constructor
        @param expression: expression minOccurs=0 maxOccurs=unbounded
        @type expression: string
        '''
        RegexValidatorBase.__init__(self, expression=expression)
