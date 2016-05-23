from core.agility.common.AgilityModelBase import AgilityModelBase

class FileSystemBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name='', maxvolumesize='', encryptionsupported=None, storagedevices=[], raidlevels=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'native': True, 'type': 'string'}, 'maxVolumeSize': {'name': 'maxvolumesize', 'native': True, 'type': 'string'}, 'encryptionSupported': {'name': 'encryptionsupported', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'storageDevices': {'name': 'storagedevices', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'FileSystemDevice'}, 'raidLevels': {'name': 'raidlevels', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}})
        self.name = name
        self.maxvolumesize = maxvolumesize
        self.encryptionsupported = encryptionsupported
        self.storagedevices = storagedevices
        self.raidlevels = raidlevels 
