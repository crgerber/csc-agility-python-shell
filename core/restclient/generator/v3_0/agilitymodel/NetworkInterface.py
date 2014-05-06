from base.NetworkInterface import NetworkInterfaceBase
from actions.NetworkInterface import NetworkInterfaceActions

class NetworkInterface(NetworkInterfaceBase, NetworkInterfaceActions):
    '''
    classdocs
    '''
    def __init__(self, network=None, physicaladdress=None, address=None):
        '''
        Constructor
        @param network: network minOccurs=0
        @type network: Link
        @param physicaladdress: physicaladdress minOccurs=0
        @type physicaladdress: string
        @param address: address minOccurs=0
        @type address: Address
        '''
        NetworkInterfaceBase.__init__(self, network=network, physicaladdress=physicaladdress, address=address)
