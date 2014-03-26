from core.agility.v2_0.agilitymodel.base.AddressList import AddressListBase
from core.agility.v2_0.agilitymodel.actions.AddressList import AddressListActions

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
