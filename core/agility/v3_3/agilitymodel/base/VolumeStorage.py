from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VolumeStorageBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, hasfilesystem=None, volumesnapshots=[], storage=[], location=None, volume=None, instance=None, unit=None, storageid=None, device=None, snapshotid=None, properties=[], cloud=None, size=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'storage': {'maxOccurs': 'unbounded', 'type': 'Storage', 'name': 'storage', 'minOccurs': '0', 'native': False}, 'volume': {'type': 'Link', 'name': 'volume', 'minOccurs': '0', 'native': False}, 'instance': {'type': 'Link', 'name': 'instance', 'minOccurs': '0', 'native': False}, 'volumeSnapshots': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'volumesnapshots', 'minOccurs': '0', 'native': False}, 'device': {'type': 'string', 'name': 'device', 'minOccurs': '0', 'native': True}, 'location': {'type': 'string', 'name': 'location', 'minOccurs': '0', 'native': True}, 'hasFileSystem': {'type': 'boolean', 'name': 'hasfilesystem', 'minOccurs': '0', 'native': True}, 'snapshotId': {'type': 'int', 'name': 'snapshotid', 'minOccurs': '0', 'native': True}, 'size': {'type': 'int', 'name': 'size', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}, 'unit': {'type': 'int', 'name': 'unit', 'minOccurs': '0', 'native': True}, 'storageId': {'type': 'string', 'name': 'storageid', 'minOccurs': '0', 'native': True}})
        self.hasfilesystem = hasfilesystem
        self.volumesnapshots = volumesnapshots
        self.storage = storage
        self.location = location
        self.volume = volume
        self.instance = instance
        self.unit = unit
        self.storageid = storageid
        self.device = device
        self.snapshotid = snapshotid
        self.properties = properties
        self.cloud = cloud
        self.size = size 
