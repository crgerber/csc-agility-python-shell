from core.agility.common.AgilityModelBase import AgilityModelBase

class GlobalVariableBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, datevalue=None, stringvalue=None, doublevalue=None, booleanvalue=None, intvalue=None, key=None, bytevalue=None, floatvalue=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'dateValue': {'name': 'datevalue', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'stringValue': {'name': 'stringvalue', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'doubleValue': {'name': 'doublevalue', 'minOccurs': '0', 'native': True, 'type': 'double'}, 'booleanValue': {'name': 'booleanvalue', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'intValue': {'name': 'intvalue', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'key': {'name': 'key', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'floatValue': {'name': 'floatvalue', 'minOccurs': '0', 'native': True, 'type': 'float'}, 'byteValue': {'name': 'bytevalue', 'minOccurs': '0', 'native': True, 'type': 'hexBinary'}})
        self.datevalue = datevalue
        self.stringvalue = stringvalue
        self.doublevalue = doublevalue
        self.booleanvalue = booleanvalue
        self.intvalue = intvalue
        self.key = key
        self.bytevalue = bytevalue
        self.floatvalue = floatvalue 
