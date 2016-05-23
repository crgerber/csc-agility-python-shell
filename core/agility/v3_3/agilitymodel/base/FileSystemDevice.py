from core.agility.common.AgilityModelBase import AgilityModelBase

class FileSystemDeviceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, cloudtype=None, device=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cloudType': {'name': 'cloudtype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'device': {'name': 'device', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.cloudtype = cloudtype
        self.device = device 
