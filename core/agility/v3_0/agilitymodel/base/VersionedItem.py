from core.agility.v3_0.agilitymodel.base.Item import ItemBase

class VersionedItemBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, slot=None, publisher=None, imagepath=None, checkoutallowed=False, publishcomment=None, slotid=None, version=None, status=None, versionstatus=None, latest=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'slot': {'type': 'string', 'name': 'slot', 'minOccurs': '0', 'native': True}, 'publisher': {'type': 'Link', 'name': 'publisher', 'minOccurs': '0', 'native': False}, 'imagePath': {'type': 'string', 'name': 'imagepath', 'minOccurs': '0', 'native': True}, 'version': {'type': 'int', 'name': 'version', 'minOccurs': '0', 'native': True}, 'publishComment': {'type': 'string', 'name': 'publishcomment', 'minOccurs': '0', 'native': True}, 'slotId': {'type': 'int', 'name': 'slotid', 'minOccurs': '0', 'native': True}, 'checkoutAllowed': {'type': 'boolean', 'name': 'checkoutallowed', 'native': True}, 'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'latest': {'type': 'boolean', 'name': 'latest', 'minOccurs': '0', 'native': True}, 'versionStatus': {'type': 'string', 'name': 'versionstatus', 'minOccurs': '0', 'native': True}})
        self.slot = slot
        self.publisher = publisher
        self.imagepath = imagepath
        self.checkoutallowed = checkoutallowed
        self.publishcomment = publishcomment
        self.slotid = slotid
        self.version = version
        self.status = status
        self.versionstatus = versionstatus
        self.latest = latest 
