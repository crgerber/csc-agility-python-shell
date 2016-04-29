from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VersionedItemBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, publishcomment=None, latest=None, versionstatus=None, slotid=None, checkoutallowed=None, slot=None, headallowed=None, version=None, imagepath=None, publisher=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'publishComment': {'native': True, 'name': 'publishcomment', 'minOccurs': '0', 'type': 'string'}, 'latest': {'native': True, 'name': 'latest', 'minOccurs': '0', 'type': 'boolean'}, 'versionStatus': {'native': True, 'name': 'versionstatus', 'minOccurs': '0', 'type': 'string'}, 'slotId': {'native': True, 'name': 'slotid', 'minOccurs': '0', 'type': 'int'}, 'checkoutAllowed': {'native': True, 'name': 'checkoutallowed', 'minOccurs': '0', 'type': 'boolean'}, 'slot': {'native': True, 'name': 'slot', 'minOccurs': '0', 'type': 'string'}, 'headAllowed': {'native': True, 'name': 'headallowed', 'minOccurs': '0', 'type': 'boolean'}, 'version': {'native': True, 'name': 'version', 'minOccurs': '0', 'type': 'int'}, 'imagePath': {'native': True, 'name': 'imagepath', 'minOccurs': '0', 'type': 'string'}, 'publisher': {'native': False, 'name': 'publisher', 'minOccurs': '0', 'type': 'Link'}})
        self.publishcomment = publishcomment
        self.latest = latest
        self.versionstatus = versionstatus
        self.slotid = slotid
        self.checkoutallowed = checkoutallowed
        self.slot = slot
        self.headallowed = headallowed
        self.version = version
        self.imagepath = imagepath
        self.publisher = publisher 
