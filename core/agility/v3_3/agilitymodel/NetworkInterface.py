from core.agility.v3_3.agilitymodel.base.NetworkInterface import NetworkInterfaceBase
from core.agility.v3_3.agilitymodel.actions.NetworkInterface import NetworkInterfaceActions

class NetworkInterface(NetworkInterfaceBase, NetworkInterfaceActions):
    '''
    classdocs
    '''
    def __init__(self, port=None, network=None, physicaladdress=None, address=None):
        '''
        Constructor
        @param port: port minOccurs=0
        @type port: Link
        @param network: network minOccurs=0
        @type network: Link
        @param physicaladdress: physicaladdress minOccurs=0
        @type physicaladdress: string
        @param address: address minOccurs=0
        @type address: Address
        '''
        NetworkInterfaceBase.__init__(self, port=port, network=network, physicaladdress=physicaladdress, address=address)
