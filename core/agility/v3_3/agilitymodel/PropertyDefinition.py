from core.agility.v3_3.agilitymodel.base.PropertyDefinition import PropertyDefinitionBase
from core.agility.v3_3.agilitymodel.actions.PropertyDefinition import PropertyDefinitionActions

class PropertyDefinition(PropertyDefinitionBase, PropertyDefinitionActions):
    '''
    classdocs
    '''
    def __init__(self, assetpropertylinkid=None, propertytype=None, minrequired=None, writable=False, validator=None, propertytypevalue=None, displayname=None, readable=False, maxallowed=None, defaultvalue=[]):
        '''
        Constructor
        @param assetpropertylinkid: assetpropertylinkid minOccurs=0
        @type assetpropertylinkid: string
        @param propertytype: propertytype minOccurs=0
        @type propertytype: Link
        @param minrequired: minrequired
        @type minrequired: int
        @param writable: writable
        @type writable: boolean
        @param validator: validator minOccurs=0
        @type validator: FieldValidators
        @param propertytypevalue: propertytypevalue minOccurs=0
        @type propertytypevalue: PropertyType
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param readable: readable
        @type readable: boolean
        @param maxallowed: maxallowed
        @type maxallowed: int
        @param defaultvalue: defaultvalue minOccurs=0 maxOccurs=unbounded
        @type defaultvalue: AssetProperty
        '''
        PropertyDefinitionBase.__init__(self, assetpropertylinkid=assetpropertylinkid, propertytype=propertytype, minrequired=minrequired, writable=writable, validator=validator, propertytypevalue=propertytypevalue, displayname=displayname, readable=readable, maxallowed=maxallowed, defaultvalue=defaultvalue)
