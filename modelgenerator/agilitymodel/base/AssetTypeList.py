from AgilityModelBase import AgilityModelBase

class AssetTypeListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, assetType=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'assetType': {'maxOccurs': 'unbounded', 'type': 'AssetType', 'name': 'assetType', 'minOccurs': '0', 'native': False}})
        self.assetType = assetType 
