from .base.AddressRangeList import AddressRangeListBase
from .actions.AddressRangeList import AddressRangeListActions

class AddressRangeList(AddressRangeListBase, AddressRangeListActions):
    '''
    classdocs
    '''
    def __init__(self, addressrange=[]):
        '''
        Constructor
        @param addressrange: addressrange minOccurs=0 maxOccurs=unbounded
        @type addressrange: AddressRange
        '''
        AddressRangeListBase.__init__(self, addressrange=addressrange)
