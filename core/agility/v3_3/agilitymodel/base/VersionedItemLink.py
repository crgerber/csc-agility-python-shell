from Link import LinkBase

class VersionedItemLinkBase(LinkBase):
    '''
    classdocs
    '''
    def __init__(self, slot=None, slotid=None, version=None, latest=None, locktype=None, versionstatus=None):
        LinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'slot': {'type': 'string', 'name': 'slot', 'minOccurs': '0', 'native': True}, 'slotId': {'type': 'int', 'name': 'slotid', 'minOccurs': '0', 'native': True}, 'version': {'type': 'int', 'name': 'version', 'minOccurs': '0', 'native': True}, 'latest': {'type': 'boolean', 'name': 'latest', 'minOccurs': '0', 'native': True}, 'lockType': {'type': 'int', 'name': 'locktype', 'minOccurs': '0', 'native': True}, 'versionStatus': {'type': 'string', 'name': 'versionstatus', 'minOccurs': '0', 'native': True}})
        self.slot = slot
        self.slotid = slotid
        self.version = version
        self.latest = latest
        self.locktype = locktype
        self.versionstatus = versionstatus 
