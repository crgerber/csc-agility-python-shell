from core.agility.v3_3.agilitymodel.base.Address import AddressBase
from core.agility.v3_3.agilitymodel.actions.Address import AddressActions

class Address(AddressBase, AddressActions):
    '''
    classdocs
    '''
    def __init__(self, address=None, elastic=None, inetaddr=None, instance=None):
        '''
        Constructor
        @param address: address minOccurs=0
        @type address: string
        @param elastic: elastic minOccurs=0
        @type elastic: boolean
        @param inetaddr: inetaddr minOccurs=0
        @type inetaddr: string
        @param instance: instance minOccurs=0
        @type instance: Link
        '''
        AddressBase.__init__(self, address=address, elastic=elastic, inetaddr=inetaddr, instance=instance)
