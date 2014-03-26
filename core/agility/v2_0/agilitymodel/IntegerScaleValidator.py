from core.agility.v2_0.agilitymodel.base.IntegerScaleValidator import IntegerScaleValidatorBase
from core.agility.v2_0.agilitymodel.actions.IntegerScaleValidator import IntegerScaleValidatorActions

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
