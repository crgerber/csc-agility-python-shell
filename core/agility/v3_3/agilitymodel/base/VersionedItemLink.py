from core.agility.v3_3.agilitymodel.base.Link import LinkBase

class VersionedItemLinkBase(LinkBase):
    '''
    classdocs
    '''
    def __init__(self, slotid=None, slot=None, versionstatus=None, latest=None, version=None, locktype=None):
        LinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'slotId': {'name': 'slotid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'slot': {'name': 'slot', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'versionStatus': {'name': 'versionstatus', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'latest': {'name': 'latest', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'version': {'name': 'version', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'lockType': {'name': 'locktype', 'minOccurs': '0', 'native': True, 'type': 'int'}})
        self.slotid = slotid
        self.slot = slot
        self.versionstatus = versionstatus
        self.latest = latest
        self.version = version
        self.locktype = locktype 
