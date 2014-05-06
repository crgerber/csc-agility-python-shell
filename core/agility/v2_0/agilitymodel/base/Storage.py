from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class StorageBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, location=None, snapshots=list(), volume=None, instance=None, unit=None, storageId=None, device=None, snapshotId=None, cloud=None, size=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'snapshots': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'snapshots', 'minOccurs': '0', 'native': False}, 'volume': {'type': 'Link', 'name': 'volume', 'minOccurs': '0', 'native': False}, 'instance': {'type': 'Link', 'name': 'instance', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}, 'location': {'type': 'string', 'name': 'location', 'minOccurs': '0', 'native': True}, 'device': {'type': 'string', 'name': 'device', 'minOccurs': '0', 'native': True}, 'snapshotId': {'type': 'int', 'name': 'snapshotId', 'minOccurs': '0', 'native': True}, 'size': {'type': 'int', 'name': 'size', 'minOccurs': '0', 'native': True}, 'unit': {'type': 'int', 'name': 'unit', 'minOccurs': '0', 'native': True}, 'storageId': {'type': 'string', 'name': 'storageId', 'minOccurs': '0', 'native': True}})
        self.location = location
        self.snapshots = snapshots
        self.volume = volume
        self.instance = instance
        self.unit = unit
        self.storageId = storageId
        self.device = device
        self.snapshotId = snapshotId
        self.cloud = cloud
        self.size = size 
