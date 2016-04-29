from core.agility.v3_3.agilitymodel.base.NetworkInterface import NetworkInterfaceBase
from core.agility.v3_3.agilitymodel.actions.NetworkInterface import NetworkInterfaceActions

class NetworkInterface(NetworkInterfaceBase, NetworkInterfaceActions):
    '''
    classdocs
    '''
    def __init__(self, physicaladdress=None, address=None, network=None, port=None):
        '''
        Constructor
        @param physicaladdress: physicaladdress minOccurs=0
        @type physicaladdress: string
        @param address: address minOccurs=0
        @type address: Address
        @param network: network minOccurs=0
        @type network: Link
        @param port: port minOccurs=0
        @type port: Link
        '''
        NetworkInterfaceBase.__init__(self, physicaladdress=physicaladdress, address=address, network=network, port=port)
