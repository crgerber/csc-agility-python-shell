from core.agility.common.AgilityModelBase import AgilityModelBase

class NetworkAddressResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, nic=None, network=None, address=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'nic': {'type': 'NetworkInterface', 'name': 'nic', 'minOccurs': '0', 'native': False}, 'network': {'type': 'Network', 'name': 'network', 'minOccurs': '0', 'native': False}, 'address': {'maxOccurs': 'unbounded', 'type': 'Address', 'name': 'address', 'minOccurs': '0', 'native': False}})
        self.nic = nic
        self.network = network
        self.address = address 
