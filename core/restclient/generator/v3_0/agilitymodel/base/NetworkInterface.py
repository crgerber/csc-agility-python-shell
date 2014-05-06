from Resource import ResourceBase

class NetworkInterfaceBase(ResourceBase):
    '''
    classdocs
    '''
    def __init__(self, network=None, physicaladdress=None, address=None):
        ResourceBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'network': {'type': 'Link', 'name': 'network', 'minOccurs': '0', 'native': False}, 'physicalAddress': {'type': 'string', 'name': 'physicaladdress', 'minOccurs': '0', 'native': True}, 'address': {'type': 'Address', 'name': 'address', 'minOccurs': '0', 'native': False}})
        self.network = network
        self.physicaladdress = physicaladdress
        self.address = address 
