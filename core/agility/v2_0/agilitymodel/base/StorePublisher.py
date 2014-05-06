from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class StorePublisherBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, url=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'url': {'type': 'string', 'name': 'url', 'minOccurs': '0', 'native': True}})
        self.url = url 
