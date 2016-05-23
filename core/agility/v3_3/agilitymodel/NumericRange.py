from core.agility.v3_3.agilitymodel.base.NumericRange import NumericRangeBase
from core.agility.v3_3.agilitymodel.actions.NumericRange import NumericRangeActions

class NumericRange(NumericRangeBase, NumericRangeActions):
    '''
    classdocs
    '''
    def __init__(self, min=None, max=None):
        '''
        Constructor
        @param min: min minOccurs=0
        @type min: string
        @param max: max minOccurs=0
        @type max: string
        '''
        NumericRangeBase.__init__(self, min=min, max=max)
