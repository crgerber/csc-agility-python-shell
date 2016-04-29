from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class ServiceBindingTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, properties=[], platformservicetype=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'platformServiceType': {'native': False, 'name': 'platformservicetype', 'minOccurs': '0', 'type': 'Link'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}})
        self.properties = properties
        self.platformservicetype = platformservicetype 
