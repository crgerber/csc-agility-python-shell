from core.agility.v3_3.agilitymodel.base.ServiceMeshList import ServiceMeshListBase

class AssetTypeListBase(ServiceMeshListBase):
    '''
    classdocs
    '''
    def __init__(self, assettype=[]):
        ServiceMeshListBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'assetType': {'maxOccurs': 'unbounded', 'native': False, 'name': 'assettype', 'minOccurs': '0', 'type': 'AssetType'}})
        self.assettype = assettype 
