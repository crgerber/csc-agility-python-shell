from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PriceEngineBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, properties=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}})
        self.properties = properties 
