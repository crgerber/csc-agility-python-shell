from ServiceMeshList import ServiceMeshListBase

class StoreProductAdapterItemListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, item=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'item': {'maxOccurs': 'unbounded', 'type': 'StoreProductAdapterItem', 'name': 'item', 'minOccurs': '0', 'native': False}})
        self.item = item 
