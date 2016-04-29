from core.agility.v3_3.agilitymodel.base.NetworkInterfaceUpdateRequest import NetworkInterfaceUpdateRequestBase
from core.agility.v3_3.agilitymodel.actions.NetworkInterfaceUpdateRequest import NetworkInterfaceUpdateRequestActions

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
