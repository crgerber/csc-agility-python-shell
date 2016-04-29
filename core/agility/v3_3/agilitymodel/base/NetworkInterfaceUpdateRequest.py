from core.agility.v3_3.agilitymodel.base.ApiRequest import ApiRequestBase

class NetworkInterfaceUpdateRequestBase(ApiRequestBase):
    '''
    classdocs
    '''
    def __init__(self, nic=None):
        ApiRequestBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'nic': {'native': False, 'name': 'nic', 'minOccurs': '0', 'type': 'NetworkInterface'}})
        self.nic = nic 
