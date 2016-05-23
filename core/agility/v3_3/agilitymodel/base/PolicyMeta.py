from core.agility.common.AgilityModelBase import AgilityModelBase

class PolicyMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, type='', availablescopes=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'name': 'type', 'native': True, 'type': 'string'}, 'availableScopes': {'name': 'availablescopes', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}})
        self.type = type
        self.availablescopes = availablescopes 
