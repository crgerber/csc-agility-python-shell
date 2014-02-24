from Item import ItemBase

class VolumeStorageBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, hasFileSystem=None, volumeSnapshots=list(), storage=list(), location=None, volume=None, instance=None, unit=None, storageId=None, device=None, snapshotId=None, cloud=None, size=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'storage': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'storage', 'minOccurs': '0', 'native': False}, 'volume': {'type': 'Link', 'name': 'volume', 'minOccurs': '0', 'native': False}, 'instance': {'type': 'Link', 'name': 'instance', 'minOccurs': '0', 'native': False}, 'volumeSnapshots': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'volumeSnapshots', 'minOccurs': '0', 'native': False}, 'device': {'type': 'string', 'name': 'device', 'minOccurs': '0', 'native': True}, 'location': {'type': 'string', 'name': 'location', 'minOccurs': '0', 'native': True}, 'hasFileSystem': {'type': 'boolean', 'name': 'hasFileSystem', 'minOccurs': '0', 'native': True}, 'snapshotId': {'type': 'int', 'name': 'snapshotId', 'minOccurs': '0', 'native': True}, 'size': {'type': 'int', 'name': 'size', 'minOccurs': '0', 'native': True}, 'unit': {'type': 'int', 'name': 'unit', 'minOccurs': '0', 'native': True}, 'storageId': {'type': 'string', 'name': 'storageId', 'minOccurs': '0', 'native': True}})
        self.hasFileSystem = hasFileSystem
        self.volumeSnapshots = volumeSnapshots
        self.storage = storage
        self.location = location
        self.volume = volume
        self.instance = instance
        self.unit = unit
        self.storageId = storageId
        self.device = device
        self.snapshotId = snapshotId
        self.cloud = cloud
        self.size = size 
