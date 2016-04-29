from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class StorageSnapshotBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, progress=None, cloud=None, storage=None, status=None, snapshotid=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'snapshotId': {'native': True, 'name': 'snapshotid', 'minOccurs': '0', 'type': 'string'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'storage': {'native': False, 'name': 'storage', 'minOccurs': '0', 'type': 'Link'}, 'status': {'native': True, 'name': 'status', 'minOccurs': '0', 'type': 'string'}, 'progress': {'native': True, 'name': 'progress', 'minOccurs': '0', 'type': 'string'}})
        self.progress = progress
        self.cloud = cloud
        self.storage = storage
        self.status = status
        self.snapshotid = snapshotid 
