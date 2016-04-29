from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class StorePublisherBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, url=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'url': {'native': True, 'name': 'url', 'minOccurs': '0', 'type': 'string'}})
        self.url = url 
