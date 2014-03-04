from core.restclient.v2_0.agilitymodel.base.Item import ItemBase

class SnapshotBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, current=None, snapshotId=None, state=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'current': {'type': 'boolean', 'name': 'current', 'minOccurs': '0', 'native': True}, 'snapshotId': {'type': 'string', 'name': 'snapshotId', 'minOccurs': '0', 'native': True}, 'state': {'type': 'State', 'name': 'state', 'minOccurs': '0', 'native': False}})
        self.current = current
        self.snapshotId = snapshotId
        self.state = state 
