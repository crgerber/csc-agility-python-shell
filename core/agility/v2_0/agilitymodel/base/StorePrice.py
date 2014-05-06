from core.agility.common.AgilityModelBase import AgilityModelBase


class StorePriceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, digits=None, labelAfter=None, recurs=None, currencyLabel=None, price=None, period=None, label=None, currency=None, threshold=None, duration=None, type=None, id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'digits': {'type': 'int', 'name': 'digits', 'minOccurs': '0', 'native': True}, 'labelAfter': {'type': 'boolean', 'name': 'labelAfter', 'minOccurs': '0', 'native': True}, 'recurs': {'type': 'int', 'name': 'recurs', 'minOccurs': '0', 'native': True}, 'price': {'type': 'double', 'name': 'price', 'minOccurs': '0', 'native': True}, 'period': {'type': 'int', 'name': 'period', 'minOccurs': '0', 'native': True}, 'label': {'type': 'string', 'name': 'label', 'minOccurs': '0', 'native': True}, 'currency': {'type': 'string', 'name': 'currency', 'minOccurs': '0', 'native': True}, 'type': {'type': 'string', 'name': 'type', 'minOccurs': '0', 'native': True}, 'threshold': {'type': 'double', 'name': 'threshold', 'minOccurs': '0', 'native': True}, 'currencyLabel': {'type': 'string', 'name': 'currencyLabel', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'duration': {'type': 'int', 'name': 'duration', 'minOccurs': '0', 'native': True}})
        self.digits = digits
        self.labelAfter = labelAfter
        self.recurs = recurs
        self.currencyLabel = currencyLabel
        self.price = price
        self.period = period
        self.label = label
        self.currency = currency
        self.threshold = threshold
        self.duration = duration
        self.type = type
        self.id = id 
