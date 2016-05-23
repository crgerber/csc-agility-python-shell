from core.agility.common.AgilityModelBase import AgilityModelBase

class NetworkAddressResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, address=[], nic=None, network=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'address': {'name': 'address', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Address'}, 'nic': {'name': 'nic', 'minOccurs': '0', 'native': False, 'type': 'NetworkInterface'}, 'network': {'name': 'network', 'minOccurs': '0', 'native': False, 'type': 'Network'}})
        self.address = address
        self.nic = nic
        self.network = network 
