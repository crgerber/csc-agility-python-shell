from core.agility.v3_3.agilitymodel.base.IntegerRange import IntegerRangeBase
from core.agility.v3_3.agilitymodel.actions.IntegerRange import IntegerRangeActions

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
