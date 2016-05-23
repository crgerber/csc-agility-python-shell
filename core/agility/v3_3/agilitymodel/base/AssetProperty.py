from core.agility.common.AgilityModelBase import AgilityModelBase

class AssetPropertyBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, datevalue=None, overridable=False, booleanvalue=None, name=None, intvalue=None, encrypted=False, description='', propertytype=None, stringvalue=None, bytevalue=None, id=None, propertydefinition=None, floatvalue=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'dateValue': {'name': 'datevalue', 'minOccurs': '0', 'native': True, 'type': 'date'}, 'overridable': {'name': 'overridable', 'native': True, 'type': 'boolean'}, 'booleanValue': {'name': 'booleanvalue', 'minOccurs': '0', 'native': True, 'type': 'boolean'}, 'name': {'name': 'name', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'intValue': {'name': 'intvalue', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'encrypted': {'name': 'encrypted', 'native': True, 'type': 'boolean'}, 'description': {'name': 'description', 'native': True, 'type': 'string'}, 'propertyType': {'name': 'propertytype', 'minOccurs': '0', 'native': False, 'type': 'Link'}, 'stringValue': {'name': 'stringvalue', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'id': {'name': 'id', 'minOccurs': '0', 'native': True, 'type': 'int'}, 'propertyDefinition': {'name': 'propertydefinition', 'minOccurs': '0', 'native': False, 'type': 'Baselink'}, 'floatValue': {'name': 'floatvalue', 'minOccurs': '0', 'native': True, 'type': 'decimal'}, 'byteValue': {'name': 'bytevalue', 'minOccurs': '0', 'native': True, 'type': 'hexBinary'}})
        self.datevalue = datevalue
        self.overridable = overridable
        self.booleanvalue = booleanvalue
        self.name = name
        self.intvalue = intvalue
        self.encrypted = encrypted
        self.description = description
        self.propertytype = propertytype
        self.stringvalue = stringvalue
        self.bytevalue = bytevalue
        self.id = id
        self.propertydefinition = propertydefinition
        self.floatvalue = floatvalue 
