from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class StoreEditionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, itemId=None, itemType=None, prices=list(), version='', build='', release=None, itemName=None, resources=list()):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'itemId': {'type': 'int', 'name': 'itemId', 'minOccurs': '0', 'native': True}, 'itemType': {'type': 'string', 'name': 'itemType', 'minOccurs': '0', 'native': True}, 'release': {'type': 'Link', 'name': 'release', 'minOccurs': '0', 'native': False}, 'version': {'type': 'string', 'name': 'version', 'native': True}, 'build': {'type': 'string', 'name': 'build', 'native': True}, 'prices': {'maxOccurs': 'unbounded', 'type': 'StorePrice', 'name': 'prices', 'minOccurs': '0', 'native': False}, 'itemName': {'type': 'string', 'name': 'itemName', 'minOccurs': '0', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'StoreResource', 'name': 'resources', 'minOccurs': '0', 'native': False}})
        self.itemId = itemId
        self.itemType = itemType
        self.prices = prices
        self.version = version
        self.build = build
        self.release = release
        self.itemName = itemName
        self.resources = resources 
