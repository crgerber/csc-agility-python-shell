from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceMetricBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, quantity=None, capacity=None, type=''):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'quantity': {'name': 'quantity', 'native': True, 'type': 'double'}, 'capacity': {'name': 'capacity', 'native': True, 'type': 'double'}, 'type': {'name': 'type', 'native': True, 'type': 'string'}})
        self.quantity = quantity
        self.capacity = capacity
        self.type = type 
