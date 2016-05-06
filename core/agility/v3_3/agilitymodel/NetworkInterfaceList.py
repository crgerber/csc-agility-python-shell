from core.agility.v3_3.agilitymodel.base.NetworkInterfaceList import NetworkInterfaceListBase
from core.agility.v3_3.agilitymodel.actions.NetworkInterfaceList import NetworkInterfaceListActions

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
