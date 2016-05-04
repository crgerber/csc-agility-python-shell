from Resource import ResourceBase

class NetworkInterfaceBase(ResourceBase):
    '''
    classdocs
    '''
    def __init__(self, port=None, network=None, physicaladdress=None, address=None):
        ResourceBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'address': {'type': 'Address', 'name': 'address', 'minOccurs': '0', 'native': False}, 'port': {'type': 'Link', 'name': 'port', 'minOccurs': '0', 'native': False}, 'physicalAddress': {'type': 'string', 'name': 'physicaladdress', 'minOccurs': '0', 'native': True}, 'network': {'type': 'Link', 'name': 'network', 'minOccurs': '0', 'native': False}})
        self.port = port
        self.network = network
        self.physicaladdress = physicaladdress
        self.address = address 
