from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class StoreProductBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, itemdetailedpath=None, numorders=None, supportinformation=None, itemname=None, shortdescription=None, publisher=None, requirements=[], build=None, releases=[], version=None, keyfeatures=None, resources=[], category=[], itemid=None, producttype=None, itemtype=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'itemDetailedPath': {'name': 'itemdetailedpath', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'numOrders': {'name': 'numorders', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'supportInformation': {'name': 'supportinformation', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'itemName': {'name': 'itemname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'publisher': {'name': 'publisher', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'itemType': {'name': 'itemtype', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'requirements': {'name': 'requirements', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}, 'releases': {'name': 'releases', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'category': {'name': 'category', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'StoreCategory'}, 'version': {'name': 'version', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'keyFeatures': {'name': 'keyfeatures', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'resources': {'name': 'resources', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'StoreResource'}, 'shortDescription': {'name': 'shortdescription', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'itemId': {'name': 'itemid', 'native': True, 'type': 'int'}, 'productType': {'name': 'producttype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'build': {'name': 'build', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.itemdetailedpath = itemdetailedpath
        self.numorders = numorders
        self.supportinformation = supportinformation
        self.itemname = itemname
        self.shortdescription = shortdescription
        self.publisher = publisher
        self.requirements = requirements
        self.build = build
        self.releases = releases
        self.version = version
        self.keyfeatures = keyfeatures
        self.resources = resources
        self.category = category
        self.itemid = itemid
        self.producttype = producttype
        self.itemtype = itemtype 
