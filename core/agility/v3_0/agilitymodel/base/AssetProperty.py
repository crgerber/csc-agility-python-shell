from core.agility.common.AgilityModelBase import AgilityModelBase


class AssetPropertyBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, description='', propertydefinition=None, encrypted=False, floatvalue=None, overridable=False, intvalue=None, datevalue=None, propertytype=None, bytevalue=None, stringvalue=None, booleanvalue=None, id=None, name=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'description': {'type': 'string', 'name': 'description', 'native': True}, 'propertyDefinition': {'type': 'Link', 'name': 'propertydefinition', 'minOccurs': '0', 'native': False}, 'encrypted': {'type': 'boolean', 'name': 'encrypted', 'native': True}, 'floatValue': {'type': 'decimal', 'name': 'floatvalue', 'minOccurs': '0', 'native': True}, 'overridable': {'type': 'boolean', 'name': 'overridable', 'native': True}, 'intValue': {'type': 'int', 'name': 'intvalue', 'minOccurs': '0', 'native': True}, 'dateValue': {'type': 'date', 'name': 'datevalue', 'minOccurs': '0', 'native': True}, 'propertyType': {'type': 'Link', 'name': 'propertytype', 'minOccurs': '0', 'native': False}, 'byteValue': {'type': 'hexBinary', 'name': 'bytevalue', 'minOccurs': '0', 'native': True}, 'stringValue': {'type': 'string', 'name': 'stringvalue', 'minOccurs': '0', 'native': True}, 'booleanValue': {'type': 'boolean', 'name': 'booleanvalue', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}})
        self.description = description
        self.propertydefinition = propertydefinition
        self.encrypted = encrypted
        self.floatvalue = floatvalue
        self.overridable = overridable
        self.intvalue = intvalue
        self.datevalue = datevalue
        self.propertytype = propertytype
        self.bytevalue = bytevalue
        self.stringvalue = stringvalue
        self.booleanvalue = booleanvalue
        self.id = id
        self.name = name 
