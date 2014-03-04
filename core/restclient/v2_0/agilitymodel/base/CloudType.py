from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class CloudTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, models=list(), type=None, properties=list()):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'models': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'models', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.models = models
        self.type = type
        self.properties = properties 
