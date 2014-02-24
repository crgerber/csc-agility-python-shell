from base.IntegerRangeValidator import IntegerRangeValidatorBase
from actions.IntegerRangeValidator import IntegerRangeValidatorActions

class IntegerRangeValidator(IntegerRangeValidatorBase, IntegerRangeValidatorActions):
    '''
    classdocs
    '''
    def __init__(self, range=list()):
        '''
        Constructor
        @param range: range minOccurs=0 maxOccurs=unbounded
        @type range: IntegerRange
        '''
        IntegerRangeValidatorBase.__init__(self, range=range)
