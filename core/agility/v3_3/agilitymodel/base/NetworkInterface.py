from core.agility.v3_3.agilitymodel.base.Resource import ResourceBase

class NetworkInterfaceBase(ResourceBase):
    '''
    classdocs
    '''
    def __init__(self, address=None, port=None, network=None, physicaladdress=None):
        ResourceBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'address': {'name': 'address', 'minOccurs': '0', 'native': False, 'type': 'Address'}, 'port': {'name': 'port', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'network': {'name': 'network', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'physicalAddress': {'name': 'physicaladdress', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.address = address
        self.port = port
        self.network = network
        self.physicaladdress = physicaladdress 
