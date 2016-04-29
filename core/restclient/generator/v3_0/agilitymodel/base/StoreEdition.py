from .Item import ItemBase

class StoreEditionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, itemid=None, itemtype=None, prices=[], version='', build='', release=None, itemname=None, resources=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'itemId': {'type': 'int', 'name': 'itemid', 'minOccurs': '0', 'native': True}, 'itemType': {'type': 'string', 'name': 'itemtype', 'minOccurs': '0', 'native': True}, 'release': {'type': 'Link', 'name': 'release', 'minOccurs': '0', 'native': False}, 'version': {'type': 'string', 'name': 'version', 'native': True}, 'build': {'type': 'string', 'name': 'build', 'native': True}, 'prices': {'maxOccurs': 'unbounded', 'type': 'StorePrice', 'name': 'prices', 'minOccurs': '0', 'native': False}, 'itemName': {'type': 'string', 'name': 'itemname', 'minOccurs': '0', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'StoreResource', 'name': 'resources', 'minOccurs': '0', 'native': False}})
        self.itemid = itemid
        self.itemtype = itemtype
        self.prices = prices
        self.version = version
        self.build = build
        self.release = release
        self.itemname = itemname
        self.resources = resources 
