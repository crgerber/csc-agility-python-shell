from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class SnapshotBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, current=None, snapshotid=None, state=None, instance=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'current': {'type': 'boolean', 'name': 'current', 'minOccurs': '0', 'native': True}, 'snapshotId': {'type': 'string', 'name': 'snapshotid', 'minOccurs': '0', 'native': True}, 'state': {'type': 'State', 'name': 'state', 'minOccurs': '0', 'native': False}, 'instance': {'type': 'Link', 'name': 'instance', 'minOccurs': '0', 'native': False}})
        self.current = current
        self.snapshotid = snapshotid
        self.state = state
        self.instance = instance 
