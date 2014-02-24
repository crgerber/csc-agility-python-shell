from AgilityModelBase import AgilityModelBase

class FileSystemDeviceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, device=None, cloudType=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'device': {'type': 'string', 'name': 'device', 'minOccurs': '0', 'native': True}, 'cloudType': {'type': 'Link', 'name': 'cloudType', 'minOccurs': '0', 'native': False}})
        self.device = device
        self.cloudType = cloudType 
