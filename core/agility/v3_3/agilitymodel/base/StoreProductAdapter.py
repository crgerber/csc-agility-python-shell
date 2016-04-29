from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class StoreProductAdapterBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, producttype=None, classname=None, url=None, resource=[]):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'productType': {'native': False, 'name': 'producttype', 'minOccurs': '0', 'type': 'Link'}, 'className': {'native': True, 'name': 'classname', 'minOccurs': '0', 'type': 'string'}, 'url': {'native': True, 'name': 'url', 'minOccurs': '0', 'type': 'string'}, 'resource': {'maxOccurs': 'unbounded', 'native': False, 'name': 'resource', 'minOccurs': '0', 'type': 'StoreResource'}})
        self.producttype = producttype
        self.classname = classname
        self.url = url
        self.resource = resource 
