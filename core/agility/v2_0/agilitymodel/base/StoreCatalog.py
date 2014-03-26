from core.agility.v2_0.agilitymodel.base.Container import ContainerBase

class StoreCatalogBase(ContainerBase):
    '''
    classdocs
    '''
    def __init__(self, products=list()):
        ContainerBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'products': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'products', 'minOccurs': '0', 'native': False}})
        self.products = products 
