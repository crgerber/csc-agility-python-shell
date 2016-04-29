from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceMetricBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, quantity=None, capacity=None, type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'quantity': {'native': True, 'name': 'quantity', 'type': 'double'}, 'capacity': {'native': True, 'name': 'capacity', 'type': 'double'}, 'type': {'native': True, 'name': 'type', 'type': 'string'}})
        self.quantity = quantity
        self.capacity = capacity
        self.type = type 
