from core.agility.common.AgilityModelBase import AgilityModelBase

class AssetMatchBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name=None, type='', property=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'name': 'name', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'type': {'name': 'type', 'native': True, 'type': 'string'}, 'property': {'name': 'property', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'PropertyMatch'}})
        self.name = name
        self.type = type
        self.property = property 
