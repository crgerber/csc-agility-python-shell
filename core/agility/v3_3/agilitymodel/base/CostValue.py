from core.agility.common.AgilityModelBase import AgilityModelBase

class CostValueBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, recurringprice=None, initialprice=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'recurringPrice': {'type': 'string', 'name': 'recurringprice', 'minOccurs': '0', 'native': True}, 'initialPrice': {'type': 'string', 'name': 'initialprice', 'minOccurs': '0', 'native': True}})
        self.recurringprice = recurringprice
        self.initialprice = initialprice 
