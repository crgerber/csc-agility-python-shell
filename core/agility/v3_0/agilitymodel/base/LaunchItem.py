from core.agility.v3_0.agilitymodel.base.Item import ItemBase

class LaunchItemBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, itemid=None, product=None, itemtype=None, type='', purchasedby=None, edition=None, state=None, purchasedon=None, path=None, prices=[], accessurilist=None, deployments=[], itemname=None, resources=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'itemId': {'type': 'int', 'name': 'itemid', 'native': True}, 'product': {'type': 'Link', 'name': 'product', 'minOccurs': '0', 'native': False}, 'itemType': {'type': 'string', 'name': 'itemtype', 'minOccurs': '0', 'native': True}, 'itemName': {'type': 'string', 'name': 'itemname', 'minOccurs': '0', 'native': True}, 'purchasedBy': {'type': 'Link', 'name': 'purchasedby', 'minOccurs': '0', 'native': False}, 'edition': {'type': 'Link', 'name': 'edition', 'minOccurs': '0', 'native': False}, 'state': {'type': 'LaunchItemState', 'name': 'state', 'minOccurs': '0', 'native': False}, 'purchasedOn': {'type': 'date', 'name': 'purchasedon', 'minOccurs': '0', 'native': True}, 'accessUriList': {'type': 'AccessUriList', 'name': 'accessurilist', 'minOccurs': '0', 'native': False}, 'prices': {'maxOccurs': 'unbounded', 'type': 'StorePrice', 'name': 'prices', 'minOccurs': '0', 'native': False}, 'path': {'type': 'string', 'name': 'path', 'minOccurs': '0', 'native': True}, 'deployments': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'deployments', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'StoreResource', 'name': 'resources', 'minOccurs': '0', 'native': False}})
        self.itemid = itemid
        self.product = product
        self.itemtype = itemtype
        self.type = type
        self.purchasedby = purchasedby
        self.edition = edition
        self.state = state
        self.purchasedon = purchasedon
        self.path = path
        self.prices = prices
        self.accessurilist = accessurilist
        self.deployments = deployments
        self.itemname = itemname
        self.resources = resources 
