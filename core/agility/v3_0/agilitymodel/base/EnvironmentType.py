from core.agility.v3_0.agilitymodel.base.Asset import AssetBase

class EnvironmentTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({})
         
