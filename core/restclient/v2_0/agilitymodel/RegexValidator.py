from core.restclient.v2_0.agilitymodel.base.RegexValidator import RegexValidatorBase
from core.restclient.v2_0.agilitymodel.actions.RegexValidator import RegexValidatorActions

class RegexValidator(RegexValidatorBase, RegexValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, expression=list()):
        '''
        Constructor
        @param expression: expression minOccurs=0 maxOccurs=unbounded
        @type expression: string
        '''
        RegexValidatorBase.__init__(self, expression=expression)
