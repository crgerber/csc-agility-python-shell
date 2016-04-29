from core.agility.v3_3.agilitymodel.base.Link import LinkBase

class VersionedItemLinkBase(LinkBase):
    '''
    classdocs
    '''
    def __init__(self, latest=None, versionstatus=None, locktype=None, slotid=None, slot=None, version=None):
        LinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'latest': {'native': True, 'name': 'latest', 'minOccurs': '0', 'type': 'boolean'}, 'versionStatus': {'native': True, 'name': 'versionstatus', 'minOccurs': '0', 'type': 'string'}, 'lockType': {'native': True, 'name': 'locktype', 'minOccurs': '0', 'type': 'int'}, 'slotId': {'native': True, 'name': 'slotid', 'minOccurs': '0', 'type': 'int'}, 'slot': {'native': True, 'name': 'slot', 'minOccurs': '0', 'type': 'string'}, 'version': {'native': True, 'name': 'version', 'minOccurs': '0', 'type': 'int'}})
        self.latest = latest
        self.versionstatus = versionstatus
        self.locktype = locktype
        self.slotid = slotid
        self.slot = slot
        self.version = version 
