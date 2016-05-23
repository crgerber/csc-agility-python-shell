from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VolumeStorageSnapshotBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, volume=None, cloud=None, status=None, snapshotid=None, storagesnapshots=[], storage=None, progress=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'volume': {'name': 'volume', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'snapshotId': {'name': 'snapshotid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'storageSnapshots': {'name': 'storagesnapshots', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'storage': {'name': 'storage', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'progress': {'name': 'progress', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.volume = volume
        self.cloud = cloud
        self.status = status
        self.snapshotid = snapshotid
        self.storagesnapshots = storagesnapshots
        self.storage = storage
        self.progress = progress 
