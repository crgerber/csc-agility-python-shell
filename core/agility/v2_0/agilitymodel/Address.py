from core.agility.v2_0.agilitymodel.base.Address import AddressBase
from core.agility.v2_0.agilitymodel.actions.Address import AddressActions

class Address(AddressBase, AddressActions):
    '''
    classdocs
    '''
    def __init__(self, instance=None, inetAddr=None, address=None):
        '''
        Constructor
        @param instance: instance minOccurs=0
        @type instance: Link
        @param inetAddr: inetAddr minOccurs=0
        @type inetAddr: string
        @param address: address minOccurs=0
        @type address: string
        '''
        AddressBase.__init__(self, instance=instance, inetAddr=inetAddr, address=address)
