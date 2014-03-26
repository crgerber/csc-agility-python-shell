from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class StoreProductAdapterBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, url=None, className=None, resource=list(), productType=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'url': {'type': 'string', 'name': 'url', 'minOccurs': '0', 'native': True}, 'className': {'type': 'string', 'name': 'className', 'minOccurs': '0', 'native': True}, 'resource': {'maxOccurs': 'unbounded', 'type': 'StoreResource', 'name': 'resource', 'minOccurs': '0', 'native': False}, 'productType': {'type': 'Link', 'name': 'productType', 'minOccurs': '0', 'native': False}})
        self.url = url
        self.className = className
        self.resource = resource
        self.productType = productType 
