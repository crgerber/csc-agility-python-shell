from core.agility.v3_3.agilitymodel.base.IntegerScaleValidator import IntegerScaleValidatorBase
from core.agility.v3_3.agilitymodel.actions.IntegerScaleValidator import IntegerScaleValidatorActions

class IntegerScaleValidator(IntegerScaleValidatorBase, IntegerScaleValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, maxdigits=None):
        '''
        Constructor
        @param maxdigits: maxdigits
        @type maxdigits: int
        '''
        IntegerScaleValidatorBase.__init__(self, maxdigits=maxdigits)
