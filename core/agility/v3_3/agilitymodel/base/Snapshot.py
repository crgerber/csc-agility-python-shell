from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class SnapshotBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, instance=None, snapshotid=None, current=None, state=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'snapshotId': {'native': True, 'name': 'snapshotid', 'minOccurs': '0', 'type': 'string'}, 'current': {'native': True, 'name': 'current', 'minOccurs': '0', 'type': 'boolean'}, 'instance': {'native': False, 'name': 'instance', 'minOccurs': '0', 'type': 'Link'}, 'state': {'native': False, 'name': 'state', 'minOccurs': '0', 'type': 'State'}})
        self.instance = instance
        self.snapshotid = snapshotid
        self.current = current
        self.state = state 
