from Item import ItemBase

class StoreProductAdapterBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, url=None, classname=None, resource=[], producttype=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'url': {'type': 'string', 'name': 'url', 'minOccurs': '0', 'native': True}, 'className': {'type': 'string', 'name': 'classname', 'minOccurs': '0', 'native': True}, 'resource': {'maxOccurs': 'unbounded', 'type': 'StoreResource', 'name': 'resource', 'minOccurs': '0', 'native': False}, 'productType': {'type': 'Link', 'name': 'producttype', 'minOccurs': '0', 'native': False}})
        self.url = url
        self.classname = classname
        self.resource = resource
        self.producttype = producttype 
