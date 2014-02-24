from base.NetworkInterfaceList import NetworkInterfaceListBase
from actions.NetworkInterfaceList import NetworkInterfaceListActions

class NetworkInterfaceList(NetworkInterfaceListBase, NetworkInterfaceListActions):
    '''
    classdocs
    '''
    def __init__(self, NetworkInterface=list()):
        '''
        Constructor
        @param NetworkInterface: NetworkInterface minOccurs=0 maxOccurs=unbounded
        @type NetworkInterface: NetworkInterface
        '''
        NetworkInterfaceListBase.__init__(self, NetworkInterface=NetworkInterface)
