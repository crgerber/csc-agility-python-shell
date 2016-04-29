from core.agility.v3_3.agilitymodel.base.Asset import AssetBase

class PropertyDefinitionBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, assetpropertylinkid=None, propertytype=None, minrequired=None, writable=False, validator=None, propertytypevalue=None, displayname=None, readable=False, maxallowed=None, defaultvalue=[]):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'defaultValue': {'maxOccurs': 'unbounded', 'native': False, 'name': 'defaultvalue', 'minOccurs': '0', 'type': 'AssetProperty'}, 'propertyType': {'native': False, 'name': 'propertytype', 'minOccurs': '0', 'type': 'Link'}, 'validator': {'native': False, 'name': 'validator', 'minOccurs': '0', 'type': 'FieldValidators'}, 'writable': {'native': True, 'name': 'writable', 'type': 'boolean'}, 'assetPropertyLinkId': {'native': True, 'name': 'assetpropertylinkid', 'minOccurs': '0', 'type': 'string'}, 'minRequired': {'native': True, 'name': 'minrequired', 'type': 'int'}, 'displayName': {'native': True, 'name': 'displayname', 'minOccurs': '0', 'type': 'string'}, 'readable': {'native': True, 'name': 'readable', 'type': 'boolean'}, 'maxAllowed': {'native': True, 'name': 'maxallowed', 'type': 'int'}, 'propertyTypeValue': {'native': False, 'name': 'propertytypevalue', 'minOccurs': '0', 'type': 'PropertyType'}})
        self.assetpropertylinkid = assetpropertylinkid
        self.propertytype = propertytype
        self.minrequired = minrequired
        self.writable = writable
        self.validator = validator
        self.propertytypevalue = propertytypevalue
        self.displayname = displayname
        self.readable = readable
        self.maxallowed = maxallowed
        self.defaultvalue = defaultvalue 
