from core.agility.common.AgilityModelBase import AgilityModelBase

class NetworkAddressResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, nic=None, address=[], network=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'address': {'maxOccurs': 'unbounded', 'native': False, 'name': 'address', 'minOccurs': '0', 'type': 'Address'}, 'nic': {'native': False, 'name': 'nic', 'minOccurs': '0', 'type': 'NetworkInterface'}, 'network': {'native': False, 'name': 'network', 'minOccurs': '0', 'type': 'Network'}})
        self.nic = nic
        self.address = address
        self.network = network 
