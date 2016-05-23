from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class StorageBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, volume=None, cloud=None, instance=None, properties=[], storageid=None, snapshots=[], snapshotid=None, size=None, device=None, unit=None, location=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'volume': {'name': 'volume', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'location': {'name': 'location', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'cloud': {'name': 'cloud', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'instance': {'name': 'instance', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'storageId': {'name': 'storageid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'snapshots': {'name': 'snapshots', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'snapshotId': {'name': 'snapshotid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'size': {'name': 'size', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'device': {'name': 'device', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'unit': {'name': 'unit', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}})
        self.volume = volume
        self.cloud = cloud
        self.instance = instance
        self.properties = properties
        self.storageid = storageid
        self.snapshots = snapshots
        self.snapshotid = snapshotid
        self.size = size
        self.device = device
        self.unit = unit
        self.location = location 
