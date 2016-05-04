from base.NetworkAddressRequest import NetworkAddressRequestBase
from actions.NetworkAddressRequest import NetworkAddressRequestActions

class NetworkAddressRequest(NetworkAddressRequestBase, NetworkAddressRequestActions):
    '''
    classdocs
    '''
    def __init__(self, networklink=None, network=None, nic=None, addresstorelease=None, instance=None, address=None, operation=None):
        '''
        Constructor
        @param networklink: networklink minOccurs=0
        @type networklink: Link
        @param network: network minOccurs=0
        @type network: Network
        @param nic: nic minOccurs=0
        @type nic: NetworkInterface
        @param addresstorelease: addresstorelease minOccurs=0
        @type addresstorelease: string
        @param instance: instance minOccurs=0
        @type instance: Instance
        @param address: address minOccurs=0
        @type address: Address
        @param operation: operation
        @type operation: AddressOperation
        '''
        NetworkAddressRequestBase.__init__(self, networklink=networklink, network=network, nic=nic, addresstorelease=addresstorelease, instance=instance, address=address, operation=operation)
