from .base.NumericScaleValidator import NumericScaleValidatorBase
from .actions.NumericScaleValidator import NumericScaleValidatorActions

class NumericScaleValidator(NumericScaleValidatorBase, NumericScaleValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, maxdigits=None, maxfractions=None):
        '''
        Constructor
        @param maxdigits: maxdigits minOccurs=0
        @type maxdigits: int
        @param maxfractions: maxfractions minOccurs=0
        @type maxfractions: int
        '''
        NumericScaleValidatorBase.__init__(self, maxdigits=maxdigits, maxfractions=maxfractions)
