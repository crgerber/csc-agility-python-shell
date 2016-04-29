from core.agility.v3_3.agilitymodel.base.NetworkAddressList import NetworkAddressListBase
from core.agility.v3_3.agilitymodel.actions.NetworkAddressList import NetworkAddressListActions

class NetworkAddressList(NetworkAddressListBase, NetworkAddressListActions):
    '''
    classdocs
    '''
    def __init__(self, requestid=None, address=[], network=None):
        '''
        Constructor
        @param requestid: requestid minOccurs=0
        @type requestid: string
        @param address: address minOccurs=0 maxOccurs=unbounded
        @type address: Address
        @param network: network
        @type network: Link
        '''
        NetworkAddressListBase.__init__(self, requestid=requestid, address=address, network=network)
