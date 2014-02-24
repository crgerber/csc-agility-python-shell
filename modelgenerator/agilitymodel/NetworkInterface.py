from base.NetworkInterface import NetworkInterfaceBase
from actions.NetworkInterface import NetworkInterfaceActions

class NetworkInterface(NetworkInterfaceBase, NetworkInterfaceActions):
    '''
    classdocs
    '''
    def __init__(self, network=None, physicalAddress=None, address=None):
        '''
        Constructor
        @param network: network minOccurs=0
        @type network: Link
        @param physicalAddress: physicalAddress minOccurs=0
        @type physicalAddress: string
        @param address: address minOccurs=0
        @type address: Address
        '''
        NetworkInterfaceBase.__init__(self, network=network, physicalAddress=physicalAddress, address=address)
