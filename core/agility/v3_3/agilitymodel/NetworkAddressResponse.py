from core.agility.v3_3.agilitymodel.base.NetworkAddressResponse import NetworkAddressResponseBase
from core.agility.v3_3.agilitymodel.actions.NetworkAddressResponse import NetworkAddressResponseActions

class NetworkAddressResponse(NetworkAddressResponseBase, NetworkAddressResponseActions):
    '''
    classdocs
    '''
    def __init__(self, address=[], nic=None, network=None):
        '''
        Constructor
        @param address: address minOccurs=0 maxOccurs=unbounded
        @type address: Address
        @param nic: nic minOccurs=0
        @type nic: NetworkInterface
        @param network: network minOccurs=0
        @type network: Network
        '''
        NetworkAddressResponseBase.__init__(self, address=address, nic=nic, network=network)
