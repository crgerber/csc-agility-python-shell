from base.Address import AddressBase
from actions.Address import AddressActions

class Address(AddressBase, AddressActions):
    '''
    classdocs
    '''
    def __init__(self, instance=None, inetaddr=None, elastic=None, address=None):
        '''
        Constructor
        @param instance: instance minOccurs=0
        @type instance: Link
        @param inetaddr: inetaddr minOccurs=0
        @type inetaddr: string
        @param elastic: elastic minOccurs=0
        @type elastic: boolean
        @param address: address minOccurs=0
        @type address: string
        '''
        AddressBase.__init__(self, instance=instance, inetaddr=inetaddr, elastic=elastic, address=address)
