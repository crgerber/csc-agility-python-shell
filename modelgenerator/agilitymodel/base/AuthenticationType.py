from Asset import AssetBase

class AuthenticationTypeBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, type='', properties=list()):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'type': 'string', 'name': 'type', 'native': True}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.type = type
        self.properties = properties 
