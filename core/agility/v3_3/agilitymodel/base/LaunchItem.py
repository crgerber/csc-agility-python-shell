from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class LaunchItemBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, edition=None, path=None, resources=[], itemid=None, state=None, type='', itemtype=None, deployments=[], accessurilist=None, purchasedon=None, itemname=None, prices=[], purchasedby=None, product=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'edition': {'native': False, 'name': 'edition', 'minOccurs': '0', 'type': 'Link'}, 'path': {'native': True, 'name': 'path', 'minOccurs': '0', 'type': 'string'}, 'resources': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resources', 'minOccurs': '0', 'type': 'StoreResource'}, 'itemId': {'native': True, 'name': 'itemid', 'type': 'int'}, 'state': {'native': False, 'name': 'state', 'minOccurs': '0', 'type': 'LaunchItemState'}, 'type': {'native': True, 'name': 'type', 'type': 'string'}, 'itemType': {'native': True, 'name': 'itemtype', 'minOccurs': '0', 'type': 'string'}, 'deployments': {'maxOccurs': 'unbounded', 'native': False, 'name': 'deployments', 'minOccurs': '0', 'type': 'Link'}, 'accessUriList': {'native': False, 'name': 'accessurilist', 'minOccurs': '0', 'type': 'AccessUriList'}, 'purchasedOn': {'native': True, 'name': 'purchasedon', 'minOccurs': '0', 'type': 'date'}, 'itemName': {'native': True, 'name': 'itemname', 'minOccurs': '0', 'type': 'string'}, 'prices': {'maxOccurs': 'unbounded', 'native': False, 'name': 'prices', 'minOccurs': '0', 'type': 'StorePrice'}, 'purchasedBy': {'native': False, 'name': 'purchasedby', 'minOccurs': '0', 'type': 'Link'}, 'product': {'native': False, 'name': 'product', 'minOccurs': '0', 'type': 'Link'}})
        self.edition = edition
        self.path = path
        self.resources = resources
        self.itemid = itemid
        self.state = state
        self.type = type
        self.itemtype = itemtype
        self.deployments = deployments
        self.accessurilist = accessurilist
        self.purchasedon = purchasedon
        self.itemname = itemname
        self.prices = prices
        self.purchasedby = purchasedby
        self.product = product 
