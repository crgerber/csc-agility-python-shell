from core.agility.common.AgilityModelBase import AgilityModelBase

class AssetMatchBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, name=None, property=[], type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'name': {'native': True, 'name': 'name', 'minOccurs': '0', 'type': 'string'}, 'property': {'maxOccurs': 'unbounded', 'native': False, 'name': 'property', 'minOccurs': '0', 'type': 'PropertyMatch'}, 'type': {'native': True, 'name': 'type', 'type': 'string'}})
        self.name = name
        self.property = property
        self.type = type 
