from core.agility.common.AgilityModelBase import AgilityModelBase

class IntegerRangeBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, max=None, min=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'max': {'native': True, 'name': 'max', 'minOccurs': '0', 'type': 'string'}, 'min': {'native': True, 'name': 'min', 'minOccurs': '0', 'type': 'string'}})
        self.max = max
        self.min = min 
