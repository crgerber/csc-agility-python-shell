from core.agility.v3_3.agilitymodel.base.ApiResponse import ApiResponseBase

class NetworkInterfaceUpdateResponseBase(ApiResponseBase):
    '''
    classdocs
    '''
    def __init__(self, nic=None):
        ApiResponseBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'nic': {'native': False, 'name': 'nic', 'minOccurs': '0', 'type': 'NetworkInterface'}})
        self.nic = nic 
