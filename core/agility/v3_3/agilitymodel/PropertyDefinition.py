from core.agility.v3_3.agilitymodel.base.PropertyDefinition import PropertyDefinitionBase
from core.agility.v3_3.agilitymodel.actions.PropertyDefinition import PropertyDefinitionActions

class PropertyDefinition(PropertyDefinitionBase, PropertyDefinitionActions):
    '''
    classdocs
    '''
    def __init__(self, assetpropertylinkid=None, writable=False, displayname=None, readable=False, propertytypevalue=None, defaultvalue=[], validator=None, minrequired=None, maxallowed=None, propertytype=None):
        '''
        Constructor
        @param assetpropertylinkid: assetpropertylinkid minOccurs=0
        @type assetpropertylinkid: string
        @param writable: writable
        @type writable: boolean
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param readable: readable
        @type readable: boolean
        @param propertytypevalue: propertytypevalue minOccurs=0
        @type propertytypevalue: PropertyType
        @param defaultvalue: defaultvalue minOccurs=0 maxOccurs=unbounded
        @type defaultvalue: AssetProperty
        @param validator: validator minOccurs=0
        @type validator: FieldValidators
        @param minrequired: minrequired
        @type minrequired: int
        @param maxallowed: maxallowed
        @type maxallowed: int
        @param propertytype: propertytype minOccurs=0
        @type propertytype: Link
        '''
        PropertyDefinitionBase.__init__(self, assetpropertylinkid=assetpropertylinkid, writable=writable, displayname=displayname, readable=readable, propertytypevalue=propertytypevalue, defaultvalue=defaultvalue, validator=validator, minrequired=minrequired, maxallowed=maxallowed, propertytype=propertytype)
