from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class StoreEditionBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, orderassettype=None, itemname=None, version='', release=None, prices=[], resources=[], itemtype=None, itemid=None, deployassettype=None, build=''):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'orderAssetType': {'name': 'orderassettype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'prices': {'name': 'prices', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'StorePrice'}, 'version': {'name': 'version', 'native': True, 'type': 'string'}, 'release': {'name': 'release', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'itemName': {'name': 'itemname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'resources': {'name': 'resources', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'StoreResource'}, 'build': {'name': 'build', 'native': True, 'type': 'string'}, 'itemId': {'name': 'itemid', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'deployAssetType': {'name': 'deployassettype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'itemType': {'name': 'itemtype', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.orderassettype = orderassettype
        self.itemname = itemname
        self.version = version
        self.release = release
        self.prices = prices
        self.resources = resources
        self.itemtype = itemtype
        self.itemid = itemid
        self.deployassettype = deployassettype
        self.build = build 
