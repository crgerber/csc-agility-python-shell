from base.CostValue import CostValueBase
from actions.CostValue import CostValueActions

class CostValue(CostValueBase, CostValueActions):
    '''
    classdocs
    '''
    def __init__(self, recurringprice=None, initialprice=None):
        '''
        Constructor
        @param recurringprice: recurringprice minOccurs=0
        @type recurringprice: string
        @param initialprice: initialprice minOccurs=0
        @type initialprice: string
        '''
        CostValueBase.__init__(self, recurringprice=recurringprice, initialprice=initialprice)
