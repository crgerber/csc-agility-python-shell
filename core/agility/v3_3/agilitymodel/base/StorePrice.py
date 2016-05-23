from core.agility.common.AgilityModelBase import AgilityModelBase

class StorePriceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, duration=None, labelafter=None, digits=None, label=None, currencylabel=None, id=None, period=None, price=None, threshold=None, recurs=None, type=None, currency=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'duration': {'name': 'duration', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'labelAfter': {'name': 'labelafter', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'digits': {'name': 'digits', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'label': {'name': 'label', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'recurs': {'name': 'recurs', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'period': {'name': 'period', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'price': {'name': 'price', 'minOccurs': '0', 'native': True, 'type': 'double'}, 'threshold': {'name': 'threshold', 'minOccurs': '0', 'native': True, 'type': 'double'}, 'currencyLabel': {'name': 'currencylabel', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'type': {'name': 'type', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'currency': {'name': 'currency', 'minOccurs': '0', 'native': True, 'type': 'string'}})
        self.duration = duration
        self.labelafter = labelafter
        self.digits = digits
        self.label = label
        self.currencylabel = currencylabel
        self.id = id
        self.period = period
        self.price = price
        self.threshold = threshold
        self.recurs = recurs
        self.type = type
        self.currency = currency 
