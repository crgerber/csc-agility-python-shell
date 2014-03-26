from core.agility.common.AgilityModelBase import AgilityModelBase


class NetworkAddressListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, network=None, requestid=None, address=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'address': {'maxOccurs': 'unbounded', 'type': 'Address', 'name': 'address', 'minOccurs': '0', 'native': False}, 'network': {'type': 'Link', 'name': 'network', 'native': False}, 'requestId': {'type': 'string', 'name': 'requestid', 'minOccurs': '0', 'native': True}})
        self.network = network
        self.requestid = requestid
        self.address = address 
