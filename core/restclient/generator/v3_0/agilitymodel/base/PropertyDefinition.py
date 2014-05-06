from Asset import AssetBase

class PropertyDefinitionBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, minrequired=None, defaultvalue=[], readable=False, writable=False, validator=None, propertytype=None, propertytypevalue=None, maxallowed=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'displayName': {'type': 'string', 'name': 'displayname', 'minOccurs': '0', 'native': True}, 'maxAllowed': {'type': 'int', 'name': 'maxallowed', 'native': True}, 'defaultValue': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'defaultvalue', 'minOccurs': '0', 'native': False}, 'readable': {'type': 'boolean', 'name': 'readable', 'native': True}, 'writable': {'type': 'boolean', 'name': 'writable', 'native': True}, 'validator': {'type': 'FieldValidators', 'name': 'validator', 'minOccurs': '0', 'native': False}, 'propertyType': {'type': 'Link', 'name': 'propertytype', 'minOccurs': '0', 'native': False}, 'propertyTypeValue': {'type': 'PropertyType', 'name': 'propertytypevalue', 'minOccurs': '0', 'native': False}, 'minRequired': {'type': 'int', 'name': 'minrequired', 'native': True}})
        self.displayname = displayname
        self.minrequired = minrequired
        self.defaultvalue = defaultvalue
        self.readable = readable
        self.writable = writable
        self.validator = validator
        self.propertytype = propertytype
        self.propertytypevalue = propertytypevalue
        self.maxallowed = maxallowed 
