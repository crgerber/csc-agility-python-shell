from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class StorageSnapshotBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, snapshotid=None, cloud=None, status=None, storage=None, progress=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'snapshotId': {'name': 'snapshotid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'status': {'name': 'status', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'storage': {'name': 'storage', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'progress': {'name': 'progress', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.snapshotid = snapshotid
        self.cloud = cloud
        self.status = status
        self.storage = storage
        self.progress = progress 
