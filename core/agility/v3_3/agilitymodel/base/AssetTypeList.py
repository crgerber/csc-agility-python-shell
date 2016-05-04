from ServiceMeshList import ServiceMeshListBase

class AssetTypeListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, assettype=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'assetType': {'maxOccurs': 'unbounded', 'type': 'AssetType', 'name': 'assettype', 'minOccurs': '0', 'native': False}})
        self.assettype = assettype 
