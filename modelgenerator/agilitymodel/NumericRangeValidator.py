from base.NumericRangeValidator import NumericRangeValidatorBase
from actions.NumericRangeValidator import NumericRangeValidatorActions

class NumericRangeValidator(NumericRangeValidatorBase, NumericRangeValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, range=list()):
        '''
        Constructor
        @param range: range minOccurs=0 maxOccurs=unbounded
        @type range: NumericRange
        '''
        NumericRangeValidatorBase.__init__(self, range=range)
