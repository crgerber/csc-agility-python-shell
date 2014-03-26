from Item import ItemBase

class StorageSnapshotBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, snapshotid=None, storage=None, cloud=None, progress=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'snapshotId': {'type': 'string', 'name': 'snapshotid', 'minOccurs': '0', 'native': True}, 'storage': {'type': 'Link', 'name': 'storage', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'progress': {'type': 'string', 'name': 'progress', 'minOccurs': '0', 'native': True}})
        self.status = status
        self.snapshotid = snapshotid
        self.storage = storage
        self.cloud = cloud
        self.progress = progress 
