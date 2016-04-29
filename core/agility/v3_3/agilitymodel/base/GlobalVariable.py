from core.agility.common.AgilityModelBase import AgilityModelBase

class GlobalVariableBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, booleanvalue=None, doublevalue=None, floatvalue=None, stringvalue=None, bytevalue=None, datevalue=None, key='', intvalue=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'booleanValue': {'native': True, 'name': 'booleanvalue', 'minOccurs': '0', 'type': 'boolean'}, 'doubleValue': {'native': True, 'name': 'doublevalue', 'minOccurs': '0', 'type': 'double'}, 'floatValue': {'native': True, 'name': 'floatvalue', 'minOccurs': '0', 'type': 'float'}, 'stringValue': {'native': True, 'name': 'stringvalue', 'minOccurs': '0', 'type': 'string'}, 'byteValue': {'native': True, 'name': 'bytevalue', 'minOccurs': '0', 'type': 'hexBinary'}, 'dateValue': {'native': True, 'name': 'datevalue', 'minOccurs': '0', 'type': 'date'}, 'key': {'native': True, 'name': 'key', 'type': 'string'}, 'intValue': {'native': True, 'name': 'intvalue', 'minOccurs': '0', 'type': 'int'}})
        self.booleanvalue = booleanvalue
        self.doublevalue = doublevalue
        self.floatvalue = floatvalue
        self.stringvalue = stringvalue
        self.bytevalue = bytevalue
        self.datevalue = datevalue
        self.key = key
        self.intvalue = intvalue 
