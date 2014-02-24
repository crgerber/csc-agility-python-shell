from Item import ItemBase

class AuthenticationBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, type=None, properties=list()):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'type': 'Link', 'name': 'type', 'native': False}, 'properties': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'properties', 'minOccurs': '0', 'native': False}})
        self.type = type
        self.properties = properties 
