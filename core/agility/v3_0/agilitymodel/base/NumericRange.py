from core.agility.common.AgilityModelBase import AgilityModelBase


class NumericRangeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, max=None, min=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'max': {'type': 'string', 'name': 'max', 'minOccurs': '0', 'native': True}, 'min': {'type': 'string', 'name': 'min', 'minOccurs': '0', 'native': True}})
        self.max = max
        self.min = min 
