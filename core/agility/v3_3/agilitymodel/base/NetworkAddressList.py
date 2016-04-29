from core.agility.common.AgilityModelBase import AgilityModelBase

class NetworkAddressListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, requestid=None, address=[], network=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'requestId': {'native': True, 'name': 'requestid', 'minOccurs': '0', 'type': 'string'}, 'address': {'maxOccurs': 'unbounded', 'native': False, 'name': 'address', 'minOccurs': '0', 'type': 'Address'}, 'network': {'native': False, 'name': 'network', 'type': 'Link'}})
        self.requestid = requestid
        self.address = address
        self.network = network 
