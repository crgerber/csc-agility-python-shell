from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VolumeStorageSnapshotBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, storagesnapshots=[], progress=None, snapshotid=None, cloud=None, storage=None, status=None, volume=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'storageSnapshots': {'maxOccurs': 'unbounded', 'native': False, 'name': 'storagesnapshots', 'minOccurs': '0', 'type': 'Link'}, 'progress': {'native': True, 'name': 'progress', 'minOccurs': '0', 'type': 'string'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'snapshotId': {'native': True, 'name': 'snapshotid', 'minOccurs': '0', 'type': 'string'}, 'storage': {'native': False, 'name': 'storage', 'minOccurs': '0', 'type': 'Link'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'volume': {'native': False, 'name': 'volume', 'minOccurs': '0', 'type': 'Link'}})
        self.storagesnapshots = storagesnapshots
        self.progress = progress
        self.snapshotid = snapshotid
        self.cloud = cloud
        self.storage = storage
        self.status = status
        self.volume = volume 
