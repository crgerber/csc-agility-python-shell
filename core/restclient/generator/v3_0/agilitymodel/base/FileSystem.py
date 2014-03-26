from AgilityModelBase import AgilityModelBase

class FileSystemBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, storagedevices=[], encryptionsupported=None, name='', raidlevels=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'storageDevices': {'maxOccurs': 'unbounded', 'type': 'FileSystemDevice', 'name': 'storagedevices', 'minOccurs': '0', 'native': False}, 'encryptionSupported': {'type': 'boolean', 'name': 'encryptionsupported', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'raidLevels': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'raidlevels', 'minOccurs': '0', 'native': True}})
        self.storagedevices = storagedevices
        self.encryptionsupported = encryptionsupported
        self.name = name
        self.raidlevels = raidlevels 
