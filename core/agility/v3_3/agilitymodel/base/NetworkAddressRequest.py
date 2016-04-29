from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class NetworkAddressRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, instance=None, networklink=None, nic=None, addresstorelease=None, address=None, operation=None, network=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'networkLink': {'native': False, 'name': 'networklink', 'minOccurs': '0', 'type': 'Link'}, 'instance': {'native': False, 'name': 'instance', 'minOccurs': '0', 'type': 'Instance'}, 'nic': {'native': False, 'name': 'nic', 'minOccurs': '0', 'type': 'NetworkInterface'}, 'address': {'native': False, 'name': 'address', 'minOccurs': '0', 'type': 'Address'}, 'addressToRelease': {'native': True, 'name': 'addresstorelease', 'minOccurs': '0', 'type': 'string'}, 'network': {'native': False, 'name': 'network', 'minOccurs': '0', 'type': 'Network'}, 'operation': {'native': False, 'name': 'operation', 'type': 'AddressOperation'}})
        self.instance = instance
        self.networklink = networklink
        self.nic = nic
        self.addresstorelease = addresstorelease
        self.address = address
        self.operation = operation
        self.network = network 
