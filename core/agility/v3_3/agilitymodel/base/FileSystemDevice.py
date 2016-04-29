from core.agility.common.AgilityModelBase import AgilityModelBase

class FileSystemDeviceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, cloudtype=None, device=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cloudType': {'native': False, 'name': 'cloudtype', 'minOccurs': '0', 'type': 'Link'}, 'device': {'native': True, 'name': 'device', 'minOccurs': '0', 'type': 'string'}})
        self.cloudtype = cloudtype
        self.device = device 
