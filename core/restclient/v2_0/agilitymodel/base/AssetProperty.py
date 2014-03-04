from core.restclient.v2_0.agilitymodel.base import AgilityModelBase


class AssetPropertyBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, description='', propertyDefinition=None, encrypted=False, floatValue=None, overridable=False, intValue=None, dateValue=None, propertyType=None, byteValue=None, stringValue=None, booleanValue=None, id=None, name=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'description': {'type': 'string', 'name': 'description', 'native': True}, 'propertyDefinition': {'type': 'Link', 'name': 'propertyDefinition', 'minOccurs': '0', 'native': False}, 'encrypted': {'type': 'boolean', 'name': 'encrypted', 'native': True}, 'floatValue': {'type': 'decimal', 'name': 'floatValue', 'minOccurs': '0', 'native': True}, 'overridable': {'type': 'boolean', 'name': 'overridable', 'native': True}, 'intValue': {'type': 'int', 'name': 'intValue', 'minOccurs': '0', 'native': True}, 'dateValue': {'type': 'date', 'name': 'dateValue', 'minOccurs': '0', 'native': True}, 'propertyType': {'type': 'Link', 'name': 'propertyType', 'minOccurs': '0', 'native': False}, 'byteValue': {'type': 'hexBinary', 'name': 'byteValue', 'minOccurs': '0', 'native': True}, 'stringValue': {'type': 'string', 'name': 'stringValue', 'minOccurs': '0', 'native': True}, 'booleanValue': {'type': 'boolean', 'name': 'booleanValue', 'minOccurs': '0', 'native': True}, 'id': {'type': 'int', 'name': 'id', 'minOccurs': '0', 'native': True}, 'name': {'type': 'string', 'name': 'name', 'minOccurs': '0', 'native': True}})
        self.description = description
        self.propertyDefinition = propertyDefinition
        self.encrypted = encrypted
        self.floatValue = floatValue
        self.overridable = overridable
        self.intValue = intValue
        self.dateValue = dateValue
        self.propertyType = propertyType
        self.byteValue = byteValue
        self.stringValue = stringValue
        self.booleanValue = booleanValue
        self.id = id
        self.name = name 
