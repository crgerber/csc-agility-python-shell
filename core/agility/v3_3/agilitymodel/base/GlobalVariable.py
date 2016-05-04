from core.agility.common.AgilityModelBase import AgilityModelBase

class GlobalVariableBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, key='', floatvalue=None, doublevalue=None, intvalue=None, datevalue=None, bytevalue=None, stringvalue=None, booleanvalue=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'key': {'type': 'string', 'name': 'key', 'native': True}, 'floatValue': {'type': 'float', 'name': 'floatvalue', 'minOccurs': '0', 'native': True}, 'doubleValue': {'type': 'double', 'name': 'doublevalue', 'minOccurs': '0', 'native': True}, 'intValue': {'type': 'int', 'name': 'intvalue', 'minOccurs': '0', 'native': True}, 'dateValue': {'type': 'date', 'name': 'datevalue', 'minOccurs': '0', 'native': True}, 'byteValue': {'type': 'hexBinary', 'name': 'bytevalue', 'minOccurs': '0', 'native': True}, 'stringValue': {'type': 'string', 'name': 'stringvalue', 'minOccurs': '0', 'native': True}, 'booleanValue': {'type': 'boolean', 'name': 'booleanvalue', 'minOccurs': '0', 'native': True}})
        self.key = key
        self.floatvalue = floatvalue
        self.doublevalue = doublevalue
        self.intvalue = intvalue
        self.datevalue = datevalue
        self.bytevalue = bytevalue
        self.stringvalue = stringvalue
        self.booleanvalue = booleanvalue 
