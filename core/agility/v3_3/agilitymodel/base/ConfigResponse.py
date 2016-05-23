from core.agility.common.AgilityModelBase import AgilityModelBase

class ConfigResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, property=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'property': {'name': 'property', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'Property'}})
        self.property = property 
