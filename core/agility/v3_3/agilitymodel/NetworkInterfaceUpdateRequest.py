from base.NetworkInterfaceUpdateRequest import NetworkInterfaceUpdateRequestBase
from actions.NetworkInterfaceUpdateRequest import NetworkInterfaceUpdateRequestActions

class NetworkInterfaceUpdateRequest(NetworkInterfaceUpdateRequestBase, NetworkInterfaceUpdateRequestActions):
    '''
    classdocs
    '''
    def __init__(self, nic=None):
        '''
        Constructor
        @param nic: nic minOccurs=0
        @type nic: NetworkInterface
        '''
        NetworkInterfaceUpdateRequestBase.__init__(self, nic=nic)
