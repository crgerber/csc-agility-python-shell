from core.agility.v3_3.agilitymodel.base.NetworkAddressRequest import NetworkAddressRequestBase
from core.agility.v3_3.agilitymodel.actions.NetworkAddressRequest import NetworkAddressRequestActions

class NetworkAddressRequest(NetworkAddressRequestBase, NetworkAddressRequestActions):
    '''
    classdocs
    '''
    def __init__(self, instance=None, networklink=None, nic=None, addresstorelease=None, address=None, operation=None, network=None):
        '''
        Constructor
        @param instance: instance minOccurs=0
        @type instance: Instance
        @param networklink: networklink minOccurs=0
        @type networklink: Link
        @param nic: nic minOccurs=0
        @type nic: NetworkInterface
        @param addresstorelease: addresstorelease minOccurs=0
        @type addresstorelease: string
        @param address: address minOccurs=0
        @type address: Address
        @param operation: operation
        @type operation: AddressOperation
        @param network: network minOccurs=0
        @type network: Network
        '''
        NetworkAddressRequestBase.__init__(self, instance=instance, networklink=networklink, nic=nic, addresstorelease=addresstorelease, address=address, operation=operation, network=network)
