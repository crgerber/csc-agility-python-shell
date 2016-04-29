from core.agility.common.AgilityModelBase import AgilityModelBase

class AssetPropertyBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, booleanvalue=None, overridable=False, floatvalue=None, propertytype=None, datevalue=None, id=None, intvalue=None, encrypted=False, description='', stringvalue=None, bytevalue=None, name=None, propertydefinition=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'booleanValue': {'native': True, 'name': 'booleanvalue', 'minOccurs': '0', 'type': 'boolean'}, 'overridable': {'native': True, 'name': 'overridable', 'type': 'boolean'}, 'propertyType': {'native': False, 'name': 'propertytype', 'minOccurs': '0', 'type': 'Link'}, 'floatValue': {'native': True, 'name': 'floatvalue', 'minOccurs': '0', 'type': 'decimal'}, 'dateValue': {'native': True, 'name': 'datevalue', 'minOccurs': '0', 'type': 'date'}, 'id': {'native': True, 'name': 'id', 'minOccurs': '0', 'type': 'int'}, 'intValue': {'native': True, 'name': 'intvalue', 'minOccurs': '0', 'type': 'int'}, 'encrypted': {'native': True, 'name': 'encrypted', 'type': 'boolean'}, 'description': {'native': True, 'name': 'description', 'type': 'string'}, 'stringValue': {'native': True, 'name': 'stringvalue', 'minOccurs': '0', 'type': 'string'}, 'byteValue': {'native': True, 'name': 'bytevalue', 'minOccurs': '0', 'type': 'hexBinary'}, 'name': {'native': True, 'name': 'name', 'minOccurs': '0', 'type': 'string'}, 'propertyDefinition': {'native': False, 'name': 'propertydefinition', 'minOccurs': '0', 'type': 'Baselink'}})
        self.booleanvalue = booleanvalue
        self.overridable = overridable
        self.floatvalue = floatvalue
        self.propertytype = propertytype
        self.datevalue = datevalue
        self.id = id
        self.intvalue = intvalue
        self.encrypted = encrypted
        self.description = description
        self.stringvalue = stringvalue
        self.bytevalue = bytevalue
        self.name = name
        self.propertydefinition = propertydefinition 
