from core.agility.v3_3.agilitymodel.base.NetworkAddressRequest import NetworkAddressRequestBase
from core.agility.v3_3.agilitymodel.actions.NetworkAddressRequest import NetworkAddressRequestActions

class NetworkAddressRequest(NetworkAddressRequestBase, NetworkAddressRequestActions):
    '''
    classdocs
    '''
    def __init__(self, address=None, network=None, operation=None, nic=None, addresstorelease=None, networklink=None, instance=None):
        '''
        Constructor
        @param address: address minOccurs=0
        @type address: Address
        @param network: network minOccurs=0
        @type network: Network
        @param operation: operation
        @type operation: AddressOperation
        @param nic: nic minOccurs=0
        @type nic: NetworkInterface
        @param addresstorelease: addresstorelease minOccurs=0
        @type addresstorelease: string
        @param networklink: networklink minOccurs=0
        @type networklink: Link
        @param instance: instance minOccurs=0
        @type instance: Instance
        '''
        NetworkAddressRequestBase.__init__(self, address=address, network=network, operation=operation, nic=nic, addresstorelease=addresstorelease, networklink=networklink, instance=instance)
