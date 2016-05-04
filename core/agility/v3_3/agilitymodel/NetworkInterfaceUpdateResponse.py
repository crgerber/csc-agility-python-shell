from base.NetworkInterfaceUpdateResponse import NetworkInterfaceUpdateResponseBase
from actions.NetworkInterfaceUpdateResponse import NetworkInterfaceUpdateResponseActions

class NetworkInterfaceUpdateResponse(NetworkInterfaceUpdateResponseBase, NetworkInterfaceUpdateResponseActions):
    '''
    classdocs
    '''
    def __init__(self, nic=None):
        '''
        Constructor
        @param nic: nic minOccurs=0
        @type nic: NetworkInterface
        '''
        NetworkInterfaceUpdateResponseBase.__init__(self, nic=nic)
