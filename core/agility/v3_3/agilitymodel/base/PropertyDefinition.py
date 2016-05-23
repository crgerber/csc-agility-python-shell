from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyDefinitionBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, assetpropertylinkid=None, writable=False, displayname=None, readable=False, propertytypevalue=None, defaultvalue=[], validator=None, minrequired=None, maxallowed=None, propertytype=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'writable': {'name': 'writable', 'native': True, 'type': 'boolean'}, 'displayName': {'name': 'displayname', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'maxAllowed': {'name': 'maxallowed', 'native': True, 'type': 'int'}, 'readable': {'name': 'readable', 'native': True, 'type': 'boolean'}, 'propertyTypeValue': {'name': 'propertytypevalue', 'minOccurs': '0', 'native': False, 'type': 'PropertyType'}, 'assetPropertyLinkId': {'name': 'assetpropertylinkid', 'minOccurs': '0', 'native': True, 'type': 'string'}, 'validator': {'name': 'validator', 'minOccurs': '0', 'native': False, 'type': 'FieldValidators'}, 'minRequired': {'name': 'minrequired', 'native': True, 'type': 'int'}, 'defaultValue': {'name': 'defaultvalue', 'native': False, 'maxOccurs': 'unbounded', 'minOccurs': '0', 'type': 'AssetProperty'}, 'propertyType': {'name': 'propertytype', 'minOccurs': '0', 'native': False, 'type': 'Link'}})
        self.assetpropertylinkid = assetpropertylinkid
        self.writable = writable
        self.displayname = displayname
        self.readable = readable
        self.propertytypevalue = propertytypevalue
        self.defaultvalue = defaultvalue
        self.validator = validator
        self.minrequired = minrequired
        self.maxallowed = maxallowed
        self.propertytype = propertytype 
