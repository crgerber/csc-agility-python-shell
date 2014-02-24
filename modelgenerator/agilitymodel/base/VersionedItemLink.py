from Link import LinkBase

class VersionedItemLinkBase(LinkBase):
    '''
    classdocs
    '''
    def __init__(self, slot=None, slotId=None, version=None, latest=None, lockType=None, versionStatus=None):
        LinkBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'slot': {'type': 'string', 'name': 'slot', 'minOccurs': '0', 'native': True}, 'slotId': {'type': 'int', 'name': 'slotId', 'minOccurs': '0', 'native': True}, 'version': {'type': 'int', 'name': 'version', 'minOccurs': '0', 'native': True}, 'latest': {'type': 'boolean', 'name': 'latest', 'minOccurs': '0', 'native': True}, 'lockType': {'type': 'int', 'name': 'lockType', 'minOccurs': '0', 'native': True}, 'versionStatus': {'type': 'string', 'name': 'versionStatus', 'minOccurs': '0', 'native': True}})
        self.slot = slot
        self.slotId = slotId
        self.version = version
        self.latest = latest
        self.lockType = lockType
        self.versionStatus = versionStatus 
