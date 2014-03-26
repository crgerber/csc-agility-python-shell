from base.PropertyDefinition import PropertyDefinitionBase
from actions.PropertyDefinition import PropertyDefinitionActions

class PropertyDefinition(PropertyDefinitionBase, PropertyDefinitionActions):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, minrequired=None, defaultvalue=[], readable=False, writable=False, validator=None, propertytype=None, propertytypevalue=None, maxallowed=None):
        '''
        Constructor
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param minrequired: minrequired
        @type minrequired: int
        @param defaultvalue: defaultvalue minOccurs=0 maxOccurs=unbounded
        @type defaultvalue: AssetProperty
        @param readable: readable
        @type readable: boolean
        @param writable: writable
        @type writable: boolean
        @param validator: validator minOccurs=0
        @type validator: FieldValidators
        @param propertytype: propertytype minOccurs=0
        @type propertytype: Link
        @param propertytypevalue: propertytypevalue minOccurs=0
        @type propertytypevalue: PropertyType
        @param maxallowed: maxallowed
        @type maxallowed: int
        '''
        PropertyDefinitionBase.__init__(self, displayname=displayname, minrequired=minrequired, defaultvalue=defaultvalue, readable=readable, writable=writable, validator=validator, propertytype=propertytype, propertytypevalue=propertytypevalue, maxallowed=maxallowed)
