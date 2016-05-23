from core.agility.v3_3.agilitymodel.base.NetworkAddressList import NetworkAddressListBase
from core.agility.v3_3.agilitymodel.actions.NetworkAddressList import NetworkAddressListActions

class NetworkAddressList(NetworkAddressListBase, NetworkAddressListActions):
    '''
    classdocs
    '''
    def __init__(self, address=[], requestid=None, network=None):
        '''
        Constructor
        @param address: address minOccurs=0 maxOccurs=unbounded
        @type address: Address
        @param requestid: requestid minOccurs=0
        @type requestid: string
        @param network: network
        @type network: Link
        '''
        NetworkAddressListBase.__init__(self, address=address, requestid=requestid, network=network)
