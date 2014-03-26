from core.agility.v3_0.agilitymodel.base.AddressList import AddressListBase
from core.agility.v3_0.agilitymodel.actions.AddressList import AddressListActions

class AddressList(AddressListBase, AddressListActions):
    '''
    classdocs
    '''
    def __init__(self, address=[]):
        '''
        Constructor
        @param address: address minOccurs=0 maxOccurs=unbounded
        @type address: Address
        '''
        AddressListBase.__init__(self, address=address)
