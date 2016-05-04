from base.NetworkAddressResponse import NetworkAddressResponseBase
from actions.NetworkAddressResponse import NetworkAddressResponseActions

class NetworkAddressResponse(NetworkAddressResponseBase, NetworkAddressResponseActions):
    '''
    classdocs
    '''
    def __init__(self, nic=None, network=None, address=[]):
        '''
        Constructor
        @param nic: nic minOccurs=0
        @type nic: NetworkInterface
        @param network: network minOccurs=0
        @type network: Network
        @param address: address minOccurs=0 maxOccurs=unbounded
        @type address: Address
        '''
        NetworkAddressResponseBase.__init__(self, nic=nic, network=network, address=address)
