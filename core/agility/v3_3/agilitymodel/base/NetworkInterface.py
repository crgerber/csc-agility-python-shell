from core.agility.v3_3.agilitymodel.base.Resource import ResourceBase

class NetworkInterfaceBase(ResourceBase):
    '''
    classdocs
    '''
    def __init__(self, physicaladdress=None, address=None, network=None, port=None):
        ResourceBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'physicalAddress': {'native': True, 'name': 'physicaladdress', 'minOccurs': '0', 'type': 'string'}, 'address': {'native': False, 'name': 'address', 'minOccurs': '0', 'type': 'Address'}, 'network': {'native': False, 'name': 'network', 'minOccurs': '0', 'type': 'Link'}, 'port': {'native': False, 'name': 'port', 'minOccurs': '0', 'type': 'Link'}})
        self.physicaladdress = physicaladdress
        self.address = address
        self.network = network
        self.port = port 
