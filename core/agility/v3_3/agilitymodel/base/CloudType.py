from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class CloudTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, properties=[], models=[], type=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'native': True, 'name': 'type', 'minOccurs': '0', 'type': 'string'}, 'models': {'maxOccurs': 'unbounded', 'native': False, 'name': 'models', 'minOccurs': '0', 'type': 'Link'}, 'properties': {'maxOccurs': 'unbounded', 'native': False, 'name': 'properties', 'minOccurs': '0', 'type': 'Property'}})
        self.properties = properties
        self.models = models
        self.type = type 
