from core.agility.common.AgilityModelBase import AgilityModelBase

class NumericRangeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, min=None, max=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'min': {'name': 'min', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'max': {'name': 'max', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.min = min
        self.max = max 
