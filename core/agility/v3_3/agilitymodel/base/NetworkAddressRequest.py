from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class NetworkAddressRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, address=None, network=None, operation=None, nic=None, addresstorelease=None, networklink=None, instance=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'nic': {'name': 'nic', 'minOccurs': '0', 'native': False, 'type': 'NetworkInterface'}, 'network': {'name': 'network', 'minOccurs': '0', 'native': False, 'type': 'Network'}, 'networkLink': {'name': 'networklink', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'address': {'name': 'address', 'minOccurs': '0', 'native': False, 'type': 'Address'}, 'addressToRelease': {'name': 'addresstorelease', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'operation': {'name': 'operation', 'native': False, 'type': 'AddressOperation'}, 'instance': {'name': 'instance', 'minOccurs': '0', 'native': False, 'type': 'Instance'}})
        self.address = address
        self.network = network
        self.operation = operation
        self.nic = nic
        self.addresstorelease = addresstorelease
        self.networklink = networklink
        self.instance = instance 
