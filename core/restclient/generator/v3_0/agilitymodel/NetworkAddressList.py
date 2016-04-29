from .base.NetworkAddressList import NetworkAddressListBase
from .actions.NetworkAddressList import NetworkAddressListActions

class NetworkAddressList(NetworkAddressListBase, NetworkAddressListActions):
    '''
    classdocs
    '''
    def __init__(self, network=None, requestid=None, address=[]):
        '''
        Constructor
        @param network: network
        @type network: Link
        @param requestid: requestid minOccurs=0
        @type requestid: string
        @param address: address minOccurs=0 maxOccurs=unbounded
        @type address: Address
        '''
        NetworkAddressListBase.__init__(self, network=network, requestid=requestid, address=address)
