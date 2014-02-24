from base.IntegerScaleValidator import IntegerScaleValidatorBase
from actions.IntegerScaleValidator import IntegerScaleValidatorActions

class IntegerScaleValidator(IntegerScaleValidatorBase, IntegerScaleValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, maxDigits=None):
        '''
        Constructor
        @param maxDigits: maxDigits
        @type maxDigits: int
        '''
        IntegerScaleValidatorBase.__init__(self, maxDigits=maxDigits)
