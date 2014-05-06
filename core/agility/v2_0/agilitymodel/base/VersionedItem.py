from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class VersionedItemBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, slot=None, publisher=None, imagePath=None, checkoutAllowed=False, publishComment=None, slotId=None, version=None, status=None, versionStatus=None, latest=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'slot': {'type': 'string', 'name': 'slot', 'minOccurs': '0', 'native': True}, 'publisher': {'type': 'Link', 'name': 'publisher', 'minOccurs': '0', 'native': False}, 'imagePath': {'type': 'string', 'name': 'imagePath', 'minOccurs': '0', 'native': True}, 'version': {'type': 'int', 'name': 'version', 'minOccurs': '0', 'native': True}, 'publishComment': {'type': 'string', 'name': 'publishComment', 'minOccurs': '0', 'native': True}, 'slotId': {'type': 'int', 'name': 'slotId', 'minOccurs': '0', 'native': True}, 'checkoutAllowed': {'type': 'boolean', 'name': 'checkoutAllowed', 'native': True}, 'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'latest': {'type': 'boolean', 'name': 'latest', 'minOccurs': '0', 'native': True}, 'versionStatus': {'type': 'string', 'name': 'versionStatus', 'minOccurs': '0', 'native': True}})
        self.slot = slot
        self.publisher = publisher
        self.imagePath = imagePath
        self.checkoutAllowed = checkoutAllowed
        self.publishComment = publishComment
        self.slotId = slotId
        self.version = version
        self.status = status
        self.versionStatus = versionStatus
        self.latest = latest 
