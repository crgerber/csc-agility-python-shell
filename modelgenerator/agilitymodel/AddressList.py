from base.AddressList import AddressListBase
from actions.AddressList import AddressListActions

class AddressList(AddressListBase, AddressListActions):
    '''
    classdocs
    '''
    def __init__(self, Address=list()):
        '''
        Constructor
        @param Address: Address minOccurs=0 maxOccurs=unbounded
        @type Address: Address
        '''
        AddressListBase.__init__(self, Address=Address)
