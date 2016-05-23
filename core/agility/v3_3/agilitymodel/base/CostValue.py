from core.agility.common.AgilityModelBase import AgilityModelBase

class CostValueBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, initialprice=None, recurringprice=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'initialPrice': {'name': 'initialprice', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'recurringPrice': {'name': 'recurringprice', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.initialprice = initialprice
        self.recurringprice = recurringprice 
