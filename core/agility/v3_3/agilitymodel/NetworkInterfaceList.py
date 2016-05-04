from base.NetworkInterfaceList import NetworkInterfaceListBase
from actions.NetworkInterfaceList import NetworkInterfaceListActions

class NetworkInterfaceList(NetworkInterfaceListBase, NetworkInterfaceListActions):
    '''
    classdocs
    '''
    def __init__(self, networkinterface=[]):
        '''
        Constructor
        @param networkinterface: networkinterface minOccurs=0 maxOccurs=unbounded
        @type networkinterface: NetworkInterface
        '''
        NetworkInterfaceListBase.__init__(self, networkinterface=networkinterface)
