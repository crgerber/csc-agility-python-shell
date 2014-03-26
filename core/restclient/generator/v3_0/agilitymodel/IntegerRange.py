from base.IntegerRange import IntegerRangeBase
from actions.IntegerRange import IntegerRangeActions

class IntegerRange(IntegerRangeBase, IntegerRangeActions):
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
        IntegerRangeBase.__init__(self, max=max, min=min)
