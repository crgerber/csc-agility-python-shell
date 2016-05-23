from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class StoreProductAdapterItemListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, item=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'item': {'name': 'item', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'StoreProductAdapterItem'}})
        self.item = item 
