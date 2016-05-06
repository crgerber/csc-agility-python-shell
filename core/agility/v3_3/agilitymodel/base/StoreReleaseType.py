from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class StoreReleaseTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({})
         
