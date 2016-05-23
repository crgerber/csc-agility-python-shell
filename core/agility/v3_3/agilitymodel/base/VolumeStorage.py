from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VolumeStorageBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, volume=None, instance=None, properties=[], size=None, volumesnapshots=[], unit=None, cloud=None, storageid=None, snapshotid=None, device=None, hasfilesystem=None, storage=[], location=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'volume': {'name': 'volume', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'location': {'name': 'location', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'instance': {'name': 'instance', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'size': {'name': 'size', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'volumeSnapshots': {'name': 'volumesnapshots', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'unit': {'name': 'unit', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'storageId': {'name': 'storageid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'snapshotId': {'name': 'snapshotid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'device': {'name': 'device', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'hasFileSystem': {'name': 'hasfilesystem', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'storage': {'name': 'storage', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Storage'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}})
        self.volume = volume
        self.instance = instance
        self.properties = properties
        self.size = size
        self.volumesnapshots = volumesnapshots
        self.unit = unit
        self.cloud = cloud
        self.storageid = storageid
        self.snapshotid = snapshotid
        self.device = device
        self.hasfilesystem = hasfilesystem
        self.storage = storage
        self.location = location 
