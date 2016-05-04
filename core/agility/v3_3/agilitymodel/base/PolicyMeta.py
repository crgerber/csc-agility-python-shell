from core.agility.common.AgilityModelBase import AgilityModelBase

class PolicyMetaBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, type='', availablescopes=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'type': 'string', 'name': 'type', 'native': True}, 'availableScopes': {'maxOccurs': 'unbounded', 'type': 'string', 'name': 'availablescopes', 'minOccurs': '0', 'native': True}})
        self.type = type
        self.availablescopes = availablescopes 
