from Item import ItemBase

class LaunchItemBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, itemId=None, product=None, itemType=None, type='', purchasedBy=None, edition=None, state=None, purchasedOn=None, path=None, prices=list(), accessUriList=None, deployments=list(), itemName=None, resources=list()):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'itemId': {'type': 'int', 'name': 'itemId', 'native': True}, 'product': {'type': 'Link', 'name': 'product', 'minOccurs': '0', 'native': False}, 'itemType': {'type': 'string', 'name': 'itemType', 'minOccurs': '0', 'native': True}, 'itemName': {'type': 'string', 'name': 'itemName', 'minOccurs': '0', 'native': True}, 'purchasedBy': {'type': 'Link', 'name': 'purchasedBy', 'minOccurs': '0', 'native': False}, 'edition': {'type': 'Link', 'name': 'edition', 'minOccurs': '0', 'native': False}, 'state': {'type': 'LaunchItemState', 'name': 'state', 'minOccurs': '0', 'native': False}, 'purchasedOn': {'type': 'date', 'name': 'purchasedOn', 'minOccurs': '0', 'native': True}, 'accessUriList': {'type': 'AccessUriList', 'name': 'accessUriList', 'minOccurs': '0', 'native': False}, 'prices': {'maxOccurs': 'unbounded', 'type': 'StorePrice', 'name': 'prices', 'minOccurs': '0', 'native': False}, 'path': {'type': 'string', 'name': 'path', 'minOccurs': '0', 'native': True}, 'deployments': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'deployments', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'native': True}, 'resources': {'maxOccurs': 'unbounded', 'type': 'StoreResource', 'name': 'resources', 'minOccurs': '0', 'native': False}})
        self.itemId = itemId
        self.product = product
        self.itemType = itemType
        self.type = type
        self.purchasedBy = purchasedBy
        self.edition = edition
        self.state = state
        self.purchasedOn = purchasedOn
        self.path = path
        self.prices = prices
        self.accessUriList = accessUriList
        self.deployments = deployments
        self.itemName = itemName
        self.resources = resources 
