from core.agility.common.AgilityModelBase import AgilityModelBase

class NetworkAddressListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, address=[], requestid=None, network=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'address': {'name': 'address', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Address'}, 'requestId': {'name': 'requestid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'network': {'name': 'network', 'native': False, 'type': 'Link'}})
        self.address = address
        self.requestid = requestid
        self.network = network 
