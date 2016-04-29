from core.agility.v3_3.agilitymodel.base.NumericScaleValidator import NumericScaleValidatorBase
from core.agility.v3_3.agilitymodel.actions.NumericScaleValidator import NumericScaleValidatorActions

class NumericScaleValidator(NumericScaleValidatorBase, NumericScaleValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, maxfractions=None, maxdigits=None):
        '''
        Constructor
        @param maxfractions: maxfractions minOccurs=0
        @type maxfractions: int
        @param maxdigits: maxdigits minOccurs=0
        @type maxdigits: int
        '''
        NumericScaleValidatorBase.__init__(self, maxfractions=maxfractions, maxdigits=maxdigits)
