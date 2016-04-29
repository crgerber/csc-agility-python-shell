from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class StoreEditionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, itemtype=None, deployassettype=None, release=None, prices=[], build='', itemid=None, version='', resources=[], itemname=None, orderassettype=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'itemType': {'native': True, 'name': 'itemtype', 'minOccurs': '0', 'type': 'string'}, 'deployAssetType': {'native': False, 'name': 'deployassettype', 'minOccurs': '0', 'type': 'Link'}, 'release': {'native': False, 'name': 'release', 'minOccurs': '0', 'type': 'Link'}, 'itemId': {'native': True, 'name': 'itemid', 'minOccurs': '0', 'type': 'int'}, 'build': {'native': True, 'name': 'build', 'type': 'string'}, 'prices': {'maxOccurs': 'unbounded', 'native': False, 'name': 'prices', 'minOccurs': '0', 'type': 'StorePrice'}, 'version': {'native': True, 'name': 'version', 'type': 'string'}, 'resources': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resources', 'minOccurs': '0', 'type': 'StoreResource'}, 'itemName': {'native': True, 'name': 'itemname', 'minOccurs': '0', 'type': 'string'}, 'orderAssetType': {'native': False, 'name': 'orderassettype', 'minOccurs': '0', 'type': 'Link'}})
        self.itemtype = itemtype
        self.deployassettype = deployassettype
        self.release = release
        self.prices = prices
        self.build = build
        self.itemid = itemid
        self.version = version
        self.resources = resources
        self.itemname = itemname
        self.orderassettype = orderassettype 
