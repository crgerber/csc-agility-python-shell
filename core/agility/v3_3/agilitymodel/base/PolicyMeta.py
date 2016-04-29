from core.agility.common.AgilityModelBase import AgilityModelBase

class PolicyMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, availablescopes=[], type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'availableScopes': {'maxOccurs': 'unbounded', 'native': True, 'name': 'availablescopes', 'minOccurs': '0', 'type': 'string'}, 'type': {'native': True, 'name': 'type', 'type': 'string'}})
        self.availablescopes = availablescopes
        self.type = type 
