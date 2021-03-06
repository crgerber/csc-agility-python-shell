from AgilityModelBase import AgilityModelBase

class AssetTypeListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, assettype=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'assetType': {'maxOccurs': 'unbounded', 'type': 'AssetType', 'name': 'assettype', 'minOccurs': '0', 'native': False}})
        self.assettype = assettype 
