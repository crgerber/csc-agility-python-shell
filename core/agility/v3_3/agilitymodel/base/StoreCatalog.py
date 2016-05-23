from core.agility.v3_3.agilitymodel.base.Container import ContainerBase

class StoreCatalogBase(ContainerBase):
    '''
    classdocs
    '''
    def __init__(self, products=[]):
        ContainerBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'products': {'name': 'products', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}})
        self.products = products 
