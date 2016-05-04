from Item import ItemBase

class StoreProductBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, category=[], publisher=None, numorders=None, keyfeatures=None, requirements=[], itemtype=None, releases=[], itemdetailedpath=None, itemid=None, version=None, build=None, producttype=None, supportinformation=None, shortdescription=None, itemname=None, resources=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'category': {'maxOccurs': 'unbounded', 'type': 'StoreCategory', 'name': 'category', 'minOccurs': '0', 'native': False}, 'publisher': {'type': 'Link', 'name': 'publisher', 'minOccurs': '0', 'native': False}, 'numOrders': {'type': 'int', 'name': 'numorders', 'minOccurs': '0', 'native': True}, 'supportInformation': {'type': 'string', 'name': 'supportinformation', 'minOccurs': '0', 'native': True}, 'requirements': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'requirements', 'minOccurs': '0', 'native': True}, 'itemType': {'type': 'string', 'name': 'itemtype', 'minOccurs': '0', 'native': True}, 'releases': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'releases', 'minOccurs': '0', 'native': False}, 'itemDetailedPath': {'type': 'string', 'name': 'itemdetailedpath', 'minOccurs': '0', 'native': True}, 'itemId': {'type': 'int', 'name': 'itemid', 'native': True}, 'version': {'type': 'string', 'name': 'version', 'minOccurs': '0', 'native': True}, 'build': {'type': 'string', 'name': 'build', 'minOccurs': '0', 'native': True}, 'productType': {'type': 'Link', 'name': 'producttype', 'minOccurs': '0', 'native': False}, 'keyFeatures': {'type': 'string', 'name': 'keyfeatures', 'minOccurs': '0', 'native': True}, 'shortDescription': {'type': 'string', 'name': 'shortdescription', 'minOccurs': '0', 'native': True}, 'itemName': {'type': 'string', 'name': 'itemname', 'minOccurs': '0', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'StoreResource', 'name': 'resources', 'minOccurs': '0', 'native': False}})
        self.category = category
        self.publisher = publisher
        self.numorders = numorders
        self.keyfeatures = keyfeatures
        self.requirements = requirements
        self.itemtype = itemtype
        self.releases = releases
        self.itemdetailedpath = itemdetailedpath
        self.itemid = itemid
        self.version = version
        self.build = build
        self.producttype = producttype
        self.supportinformation = supportinformation
        self.shortdescription = shortdescription
        self.itemname = itemname
        self.resources = resources 
