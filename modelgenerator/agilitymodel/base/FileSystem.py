from AgilityModelBase import AgilityModelBase

class FileSystemBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, storageDevices=list(), encryptionSupported=None, name='', raidLevels=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'storageDevices': {'maxOccurs': 'unbounded', 'type': 'FileSystemDevice', 'name': 'storageDevices', 'minOccurs': '0', 'native': False}, 'encryptionSupported': {'type': 'boolean', 'name': 'encryptionSupported', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'raidLevels': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'raidLevels', 'minOccurs': '0', 'native': True}})
        self.storageDevices = storageDevices
        self.encryptionSupported = encryptionSupported
        self.name = name
        self.raidLevels = raidLevels 
