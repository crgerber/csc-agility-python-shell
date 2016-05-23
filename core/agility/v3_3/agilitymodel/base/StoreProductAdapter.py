from core.agility.v3_3.agilitymodel.base.Item import ItemBase

class StoreProductAdapterBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, resource=[], url=None, producttype=None, classname=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'className': {'name': 'classname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'url': {'name': 'url', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'productType': {'name': 'producttype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'resource': {'name': 'resource', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'StoreResource'}})
        self.resource = resource
        self.url = url
        self.producttype = producttype
        self.classname = classname 
