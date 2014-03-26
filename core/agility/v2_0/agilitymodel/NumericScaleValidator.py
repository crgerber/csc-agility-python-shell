from core.agility.v2_0.agilitymodel.base.NumericScaleValidator import NumericScaleValidatorBase
from core.agility.v2_0.agilitymodel.actions.NumericScaleValidator import NumericScaleValidatorActions

class NumericScaleValidator(NumericScaleValidatorBase, NumericScaleValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, maxDigits=None, maxFractions=None):
        '''
        Constructor
        @param maxDigits: maxDigits minOccurs=0
        @type maxDigits: int
        @param maxFractions: maxFractions minOccurs=0
        @type maxFractions: int
        '''
        NumericScaleValidatorBase.__init__(self, maxDigits=maxDigits, maxFractions=maxFractions)
