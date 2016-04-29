from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class StoreProductBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, keyfeatures=None, releases=[], itemtype=None, resources=[], itemid=None, shortdescription=None, supportinformation=None, category=[], producttype=None, numorders=None, itemdetailedpath=None, build=None, version=None, itemname=None, requirements=[], publisher=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'keyFeatures': {'native': True, 'name': 'keyfeatures', 'minOccurs': '0', 'type': 'string'}, 'productType': {'native': False, 'name': 'producttype', 'minOccurs': '0', 'type': 'Link'}, 'resources': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resources', 'minOccurs': '0', 'type': 'StoreResource'}, 'itemId': {'native': True, 'name': 'itemid', 'type': 'int'}, 'shortDescription': {'native': True, 'name': 'shortdescription', 'minOccurs': '0', 'type': 'string'}, 'releases': {'maxOccurs': 'unbounded', 'native': False, 'name': 'releases', 'minOccurs': '0', 'type': 'Link'}, 'category': {'maxOccurs': 'unbounded', 'native': False, 'name': 'category', 'minOccurs': '0', 'type': 'StoreCategory'}, 'itemType': {'native': True, 'name': 'itemtype', 'minOccurs': '0', 'type': 'string'}, 'numOrders': {'native': True, 'name': 'numorders', 'minOccurs': '0', 'type': 'int'}, 'publisher': {'native': False, 'name': 'publisher', 'minOccurs': '0', 'type': 'Link'}, 'supportInformation': {'native': True, 'name': 'supportinformation', 'minOccurs': '0', 'type': 'string'}, 'build': {'native': True, 'name': 'build', 'minOccurs': '0', 'type': 'string'}, 'version': {'native': True, 'name': 'version', 'minOccurs': '0', 'type': 'string'}, 'itemName': {'native': True, 'name': 'itemname', 'minOccurs': '0', 'type': 'string'}, 'requirements': {'maxOccurs': 'unbounded', 'native': True, 'name': 'requirements', 'minOccurs': '0', 'type': 'string'}, 'itemDetailedPath': {'native': True, 'name': 'itemdetailedpath', 'minOccurs': '0', 'type': 'string'}})
        self.keyfeatures = keyfeatures
        self.releases = releases
        self.itemtype = itemtype
        self.resources = resources
        self.itemid = itemid
        self.shortdescription = shortdescription
        self.supportinformation = supportinformation
        self.category = category
        self.producttype = producttype
        self.numorders = numorders
        self.itemdetailedpath = itemdetailedpath
        self.build = build
        self.version = version
        self.itemname = itemname
        self.requirements = requirements
        self.publisher = publisher 
