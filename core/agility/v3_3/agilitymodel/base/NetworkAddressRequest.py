from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class NetworkAddressRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, networklink=None, network=None, nic=None, addresstorelease=None, instance=None, address=None, operation=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'networkLink': {'type': 'Link', 'name': 'networklink', 'minOccurs': '0', 'native': False}, 'network': {'type': 'Network', 'name': 'network', 'minOccurs': '0', 'native': False}, 'nic': {'type': 'NetworkInterface', 'name': 'nic', 'minOccurs': '0', 'native': False}, 'addressToRelease': {'type': 'string', 'name': 'addresstorelease', 'minOccurs': '0', 'native': True}, 'instance': {'type': 'Instance', 'name': 'instance', 'minOccurs': '0', 'native': False}, 'address': {'type': 'Address', 'name': 'address', 'minOccurs': '0', 'native': False}, 'operation': {'type': 'AddressOperation', 'name': 'operation', 'native': False}})
        self.networklink = networklink
        self.network = network
        self.nic = nic
        self.addresstorelease = addresstorelease
        self.instance = instance
        self.address = address
        self.operation = operation 
