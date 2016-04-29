from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VolumeStorageBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, location=None, storage=[], properties=[], instance=None, storageid=None, volumesnapshots=[], volume=None, unit=None, size=None, cloud=None, snapshotid=None, hasfilesystem=None, device=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'location': {'native': True, 'name': 'location', 'minOccurs': '0', 'type': 'string'}, 'instance': {'native': False, 'name': 'instance', 'minOccurs': '0', 'type': 'Link'}, 'hasFileSystem': {'native': True, 'name': 'hasfilesystem', 'minOccurs': '0', 'type': 'boolean'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'storage': {'maxOccurs': 'unbounded', 'native': False, 'name': 'storage', 'minOccurs': '0', 'type': 'Storage'}, 'volumeSnapshots': {'maxOccurs': 'unbounded', 'native': False, 'name': 'volumesnapshots', 'minOccurs': '0', 'type': 'Link'}, 'unit': {'native': True, 'name': 'unit', 'minOccurs': '0', 'type': 'int'}, 'size': {'native': True, 'name': 'size', 'minOccurs': '0', 'type': 'int'}, 'snapshotId': {'native': True, 'name': 'snapshotid', 'minOccurs': '0', 'type': 'int'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'storageId': {'native': True, 'name': 'storageid', 'minOccurs': '0', 'type': 'string'}, 'volume': {'native': False, 'name': 'volume', 'minOccurs': '0', 'type': 'Link'}, 'device': {'native': True, 'name': 'device', 'minOccurs': '0', 'type': 'string'}})
        self.location = location
        self.storage = storage
        self.properties = properties
        self.instance = instance
        self.storageid = storageid
        self.volumesnapshots = volumesnapshots
        self.volume = volume
        self.unit = unit
        self.size = size
        self.cloud = cloud
        self.snapshotid = snapshotid
        self.hasfilesystem = hasfilesystem
        self.device = device 
