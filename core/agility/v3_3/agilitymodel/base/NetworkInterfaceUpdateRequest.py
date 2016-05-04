from ApiRequest import ApiRequestBase

class NetworkInterfaceUpdateRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, nic=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'nic': {'type': 'NetworkInterface', 'name': 'nic', 'minOccurs': '0', 'native': False}})
        self.nic = nic 
