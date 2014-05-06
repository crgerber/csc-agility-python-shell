from core.agility.v3_0.agilitymodel.base.Item import ItemBase

class StoreProductBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, category=[], publisher=None, itemname=None, itemtype=None, releases=[], itemdetailedpath=None, itemid=None, numreviews=None, version=None, build=None, producttype=None, shortdescription=None, resources=[], averagerating=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'category': {'maxOccurs': 'unbounded', 'type': 'StoreCategory', 'name': 'category', 'minOccurs': '0', 'native': False}, 'publisher': {'type': 'Link', 'name': 'publisher', 'minOccurs': '0', 'native': False}, 'shortDescription': {'type': 'string', 'name': 'shortdescription', 'minOccurs': '0', 'native': True}, 'itemType': {'type': 'string', 'name': 'itemtype', 'minOccurs': '0', 'native': True}, 'releases': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'releases', 'minOccurs': '0', 'native': False}, 'itemDetailedPath': {'type': 'string', 'name': 'itemdetailedpath', 'minOccurs': '0', 'native': True}, 'itemId': {'type': 'int', 'name': 'itemid', 'native': True}, 'numReviews': {'type': 'int', 'name': 'numreviews', 'minOccurs': '0', 'native': True}, 'version': {'type': 'string', 'name': 'version', 'minOccurs': '0', 'native': True}, 'build': {'type': 'string', 'name': 'build', 'minOccurs': '0', 'native': True}, 'productType': {'type': 'Link', 'name': 'producttype', 'minOccurs': '0', 'native': False}, 'itemName': {'type': 'string', 'name': 'itemname', 'minOccurs': '0', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'StoreResource', 'name': 'resources', 'minOccurs': '0', 'native': False}, 'averageRating': {'type': 'decimal', 'name': 'averagerating', 'native': True}})
        self.category = category
        self.publisher = publisher
        self.itemname = itemname
        self.itemtype = itemtype
        self.releases = releases
        self.itemdetailedpath = itemdetailedpath
        self.itemid = itemid
        self.numreviews = numreviews
        self.version = version
        self.build = build
        self.producttype = producttype
        self.shortdescription = shortdescription
        self.resources = resources
        self.averagerating = averagerating 
