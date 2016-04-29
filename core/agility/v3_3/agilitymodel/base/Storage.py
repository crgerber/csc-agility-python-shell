from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class StorageBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, location=None, unit=None, device=None, size=None, snapshotid=None, snapshots=[], cloud=None, storageid=None, instance=None, volume=None, properties=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'location': {'native': True, 'name': 'location', 'minOccurs': '0', 'type': 'string'}, 'unit': {'native': True, 'name': 'unit', 'minOccurs': '0', 'type': 'int'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}, 'size': {'native': True, 'name': 'size', 'minOccurs': '0', 'type': 'int'}, 'cloud': {'native': False, 'name': 'cloud', 'minOccurs': '0', 'type': 'Link'}, 'snapshots': {'maxOccurs': 'unbounded', 'native': False, 'name': 'snapshots', 'minOccurs': '0', 'type': 'Link'}, 'snapshotId': {'native': True, 'name': 'snapshotid', 'minOccurs': '0', 'type': 'int'}, 'device': {'native': True, 'name': 'device', 'minOccurs': '0', 'type': 'string'}, 'instance': {'native': False, 'name': 'instance', 'minOccurs': '0', 'type': 'Link'}, 'storageId': {'native': True, 'name': 'storageid', 'minOccurs': '0', 'type': 'string'}, 'volume': {'native': False, 'name': 'volume', 'minOccurs': '0', 'type': 'Link'}})
        self.location = location
        self.unit = unit
        self.device = device
        self.size = size
        self.snapshotid = snapshotid
        self.snapshots = snapshots
        self.cloud = cloud
        self.storageid = storageid
        self.instance = instance
        self.volume = volume
        self.properties = properties 
