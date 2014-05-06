from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class StoreProductBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, category=list(), publisher=None, itemName=None, itemType=None, releases=list(), itemDetailedPath=None, itemId=None, numReviews=None, version=None, build=None, productType=None, shortDescription=None, resources=list(), averageRating=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'category': {'maxOccurs': 'unbounded', 'type': 'StoreCategory', 'name': 'category', 'minOccurs': '0', 'native': False}, 'publisher': {'type': 'Link', 'name': 'publisher', 'minOccurs': '0', 'native': False}, 'shortDescription': {'type': 'string', 'name': 'shortDescription', 'minOccurs': '0', 'native': True}, 'itemType': {'type': 'string', 'name': 'itemType', 'minOccurs': '0', 'native': True}, 'releases': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'releases', 'minOccurs': '0', 'native': False}, 'itemDetailedPath': {'type': 'string', 'name': 'itemDetailedPath', 'minOccurs': '0', 'native': True}, 'itemId': {'type': 'int', 'name': 'itemId', 'native': True}, 'numReviews': {'type': 'int', 'name': 'numReviews', 'minOccurs': '0', 'native': True}, 'version': {'type': 'string', 'name': 'version', 'minOccurs': '0', 'native': True}, 'build': {'type': 'string', 'name': 'build', 'minOccurs': '0', 'native': True}, 'productType': {'type': 'Link', 'name': 'productType', 'minOccurs': '0', 'native': False}, 'itemName': {'type': 'string', 'name': 'itemName', 'minOccurs': '0', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'StoreResource', 'name': 'resources', 'minOccurs': '0', 'native': False}, 'averageRating': {'type': 'decimal', 'name': 'averageRating', 'native': True}})
        self.category = category
        self.publisher = publisher
        self.itemName = itemName
        self.itemType = itemType
        self.releases = releases
        self.itemDetailedPath = itemDetailedPath
        self.itemId = itemId
        self.numReviews = numReviews
        self.version = version
        self.build = build
        self.productType = productType
        self.shortDescription = shortDescription
        self.resources = resources
        self.averageRating = averageRating 
