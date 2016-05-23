from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class VersionedItemBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, slotid=None, slot=None, versionstatus=None, publisher=None, latest=None, version=None, headallowed=None, imagepath=None, checkoutallowed=None, publishcomment=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'slotId': {'name': 'slotid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'slot': {'name': 'slot', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'versionStatus': {'name': 'versionstatus', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'publisher': {'name': 'publisher', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'latest': {'name': 'latest', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'version': {'name': 'version', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'headAllowed': {'name': 'headallowed', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'imagePath': {'name': 'imagepath', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'checkoutAllowed': {'name': 'checkoutallowed', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'publishComment': {'name': 'publishcomment', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.slotid = slotid
        self.slot = slot
        self.versionstatus = versionstatus
        self.publisher = publisher
        self.latest = latest
        self.version = version
        self.headallowed = headallowed
        self.imagepath = imagepath
        self.checkoutallowed = checkoutallowed
        self.publishcomment = publishcomment 
