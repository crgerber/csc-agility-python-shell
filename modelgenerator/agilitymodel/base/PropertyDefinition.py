from Asset import AssetBase

class PropertyDefinitionBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, displayName=None, minRequired=None, defaultValue=list(), readable=False, writable=False, validator=None, propertyType=None, propertyTypeValue=None, maxAllowed=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayName', 'minOccurs': '0', 'native': True}, 'maxAllowed': {'type': 'int', 'name': 'maxAllowed', 'native': True}, 'defaultValue': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'defaultValue', 'minOccurs': '0', 'native': False}, 'readable': {'type': 'boolean', 'name': 'readable', 'native': True}, 'writable': {'type': 'boolean', 'name': 'writable', 'native': True}, 'validator': {'type': 'FieldValidators', 'name': 'validator', 'minOccurs': '0', 'native': False}, 'propertyType': {'type': 'Link', 'name': 'propertyType', 'minOccurs': '0', 'native': False}, 'propertyTypeValue': {'type': 'PropertyType', 'name': 'propertyTypeValue', 'minOccurs': '0', 'native': False}, 'minRequired': {'type': 'int', 'name': 'minRequired', 'native': True}})
        self.displayName = displayName
        self.minRequired = minRequired
        self.defaultValue = defaultValue
        self.readable = readable
        self.writable = writable
        self.validator = validator
        self.propertyType = propertyType
        self.propertyTypeValue = propertyTypeValue
        self.maxAllowed = maxAllowed 
