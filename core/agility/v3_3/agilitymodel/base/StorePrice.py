from core.agility.common.AgilityModelBase import AgilityModelBase

class StorePriceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, currency=None, recurs=None, label=None, digits=None, id=None, period=None, threshold=None, currencylabel=None, labelafter=None, price=None, duration=None, type=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'currency': {'native': True, 'name': 'currency', 'minOccurs': '0', 'type': 'string'}, 'recurs': {'native': True, 'name': 'recurs', 'minOccurs': '0', 'type': 'int'}, 'label': {'native': True, 'name': 'label', 'minOccurs': '0', 'type': 'string'}, 'digits': {'native': True, 'name': 'digits', 'minOccurs': '0', 'type': 'int'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}, 'period': {'native': True, 'name': 'period', 'minOccurs': '0', 'type': 'int'}, 'threshold': {'native': True, 'name': 'threshold', 'minOccurs': '0', 'type': 'double'}, 'currencyLabel': {'native': True, 'name': 'currencylabel', 'minOccurs': '0', 'type': 'string'}, 'labelAfter': {'native': True, 'name': 'labelafter', 'minOccurs': '0', 'type': 'boolean'}, 'price': {'native': True, 'name': 'price', 'minOccurs': '0', 'type': 'double'}, 'duration': {'native': True, 'name': 'duration', 'minOccurs': '0', 'type': 'int'}, 'type': {'native': True, 'name': 'type', 'minOccurs': '0', 'type': 'string'}})
        self.currency = currency
        self.recurs = recurs
        self.label = label
        self.digits = digits
        self.id = id
        self.period = period
        self.threshold = threshold
        self.currencylabel = currencylabel
        self.labelafter = labelafter
        self.price = price
        self.duration = duration
        self.type = type 
