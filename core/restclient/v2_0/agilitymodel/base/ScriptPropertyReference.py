from core.restclient.v2_0.agilitymodel.base.Asset import AssetBase

class ScriptPropertyReferenceBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, type=list(), propertyDefinition=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'type', 'minOccurs': '0', 'native': False}, 'propertyDefinition': {'type': 'Link', 'name': 'propertyDefinition', 'minOccurs': '0', 'native': False}})
        self.type = type
        self.propertyDefinition = propertyDefinition 
