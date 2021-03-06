from core.agility.v3_0.agilitymodel.base.Asset import AssetBase

class CloudTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, models=[], type=None, properties=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'models': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'models', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.models = models
        self.type = type
        self.properties = properties 
