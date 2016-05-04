from core.agility.common.AgilityModelBase import AgilityModelBase

class ConfigResponseBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, property=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'property': {'maxOccurs': 'unbounded', 'type': 'Property', 'name': 'property', 'minOccurs': '0', 'native': False}})
        self.property = property 
