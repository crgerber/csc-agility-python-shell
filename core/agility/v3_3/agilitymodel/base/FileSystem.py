from core.agility.common.AgilityModelBase import AgilityModelBase

class FileSystemBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, storagedevices=[], name='', encryptionsupported=None, raidlevels=[], maxvolumesize=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'storageDevices': {'maxOccurs': 'unbounded', 'native': False, 'name': 'storagedevices', 'minOccurs': '0', 'type': 'FileSystemDevice'}, 'name': {'native': True, 'name': 'name', 'type': 'string'}, 'encryptionSupported': {'native': True, 'name': 'encryptionsupported', 'minOccurs': '0', 'type': 'boolean'}, 'raidLevels': {'maxOccurs': 'unbounded', 'native': True, 'name': 'raidlevels', 'minOccurs': '0', 'type': 'string'}, 'maxVolumeSize': {'native': True, 'name': 'maxvolumesize', 'type': 'string'}})
        self.storagedevices = storagedevices
        self.name = name
        self.encryptionsupported = encryptionsupported
        self.raidlevels = raidlevels
        self.maxvolumesize = maxvolumesize 
