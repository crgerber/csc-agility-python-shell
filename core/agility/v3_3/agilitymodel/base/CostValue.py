from core.agility.common.AgilityModelBase import AgilityModelBase

class CostValueBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, recurringprice=None, initialprice=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'recurringPrice': {'native': True, 'name': 'recurringprice', 'minOccurs': '0', 'type': 'string'}, 'initialPrice': {'native': True, 'name': 'initialprice', 'minOccurs': '0', 'type': 'string'}})
        self.recurringprice = recurringprice
        self.initialprice = initialprice 
