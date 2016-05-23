from core.agility.common.AgilityModelBase import AgilityModelBase

class ConfigRequestBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, property=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'property': {'name': 'property', 'native': True, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'string'}})
        self.property = property 
