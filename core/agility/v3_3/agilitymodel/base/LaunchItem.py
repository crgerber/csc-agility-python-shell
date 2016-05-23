from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class LaunchItemBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, product=None, itemname=None, purchasedby=None, purchasedon=None, state=None, prices=[], edition=None, path=None, accessurilist=None, resources=[], deployments=[], itemid=None, type='', itemtype=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'product': {'name': 'product', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'itemName': {'name': 'itemname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'purchasedBy': {'name': 'purchasedby', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'purchasedOn': {'name': 'purchasedon', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'state': {'name': 'state', 'minOccurs': '0', 'native': False, 'type': 'LaunchItemState'}, 'prices': {'name': 'prices', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'StorePrice'}, 'edition': {'name': 'edition', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'path': {'name': 'path', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'accessUriList': {'name': 'accessurilist', 'minOccurs': '0', 'native': False, 'type': 'AccessUriList'}, 'resources': {'name': 'resources', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'StoreResource'}, 'itemType': {'name': 'itemtype', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'itemId': {'name': 'itemid', 'native': True, 'type': 'int'}, 'type': {'name': 'type', 'native': True, 'type': 'string'}, 'deployments': {'name': 'deployments', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.product = product
        self.itemname = itemname
        self.purchasedby = purchasedby
        self.purchasedon = purchasedon
        self.state = state
        self.prices = prices
        self.edition = edition
        self.path = path
        self.accessurilist = accessurilist
        self.resources = resources
        self.deployments = deployments
        self.itemid = itemid
        self.type = type
        self.itemtype = itemtype 
