from base.NumericRange import NumericRangeBase
from actions.NumericRange import NumericRangeActions

class NumericRange(NumericRangeBase, NumericRangeActions):
    '''
    classdocs
    '''
    def __init__(self, max=None, min=None):
        '''
        Constructor
        @param max: max minOccurs=0
        @type max: string
        @param min: min minOccurs=0
        @type min: string
        '''
        NumericRangeBase.__init__(self, max=max, min=min)
