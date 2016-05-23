from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class CloudTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, models=[], type=None, properties=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'models': {'name': 'models', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Link'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'properties': {'name': 'properties', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}})
        self.models = models
        self.type = type
        self.properties = properties 
