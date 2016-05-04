from core.agility.common.AgilityModelBase import AgilityModelBase

class ResourceMetricBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, capacity=None, type='', quantity=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'type': {'type': 'string', 'name': 'type', 'native': True}, 'capacity': {'type': 'double', 'name': 'capacity', 'native': True}, 'quantity': {'type': 'double', 'name': 'quantity', 'native': True}})
        self.capacity = capacity
        self.type = type
        self.quantity = quantity 
