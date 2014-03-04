from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class StoreProductTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({})
         
