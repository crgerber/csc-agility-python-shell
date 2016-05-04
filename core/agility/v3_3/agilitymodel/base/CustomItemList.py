from ServiceMeshList import ServiceMeshListBase

class CustomItemListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, customitem=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'customItem': {'maxOccurs': 'unbounded', 'type': 'CustomItem', 'name': 'customitem', 'minOccurs': '0', 'native': False}})
        self.customitem = customitem 
