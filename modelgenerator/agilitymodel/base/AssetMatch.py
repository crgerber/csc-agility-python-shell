from AgilityModelBase import AgilityModelBase

class AssetMatchBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, property=list(), type='', name=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'property': {'maxOccurs': 'unbounded', 'type': 'PropertyMatch', 'name': 'property', 'minOccurs': '0', 'native': False}, 'type': {'type': 'string', 'name': 'type', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}})
        self.property = property
        self.type = type
        self.name = name 
