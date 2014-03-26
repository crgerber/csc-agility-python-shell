from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class StoreCategoryBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({})
         
