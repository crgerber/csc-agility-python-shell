from core.restclient.v2_0.agilitymodel.base.PropertyDefinition import PropertyDefinitionBase
from core.restclient.v2_0.agilitymodel.actions.PropertyDefinition import PropertyDefinitionActions

class PropertyDefinition(PropertyDefinitionBase, PropertyDefinitionActions):
    '''
    classdocs
    '''
    def __init__(self, displayName=None, minRequired=None, defaultValue=list(), readable=False, writable=False, validator=None, propertyType=None, propertyTypeValue=None, maxAllowed=None):
        '''
        Constructor
        @param displayName: displayName minOccurs=0
        @type displayName: string
        @param minRequired: minRequired
        @type minRequired: int
        @param defaultValue: defaultValue minOccurs=0 maxOccurs=unbounded
        @type defaultValue: AssetProperty
        @param readable: readable
        @type readable: boolean
        @param writable: writable
        @type writable: boolean
        @param validator: validator minOccurs=0
        @type validator: FieldValidators
        @param propertyType: propertyType minOccurs=0
        @type propertyType: Link
        @param propertyTypeValue: propertyTypeValue minOccurs=0
        @type propertyTypeValue: PropertyType
        @param maxAllowed: maxAllowed
        @type maxAllowed: int
        '''
        PropertyDefinitionBase.__init__(self, displayName=displayName, minRequired=minRequired, defaultValue=defaultValue, readable=readable, writable=writable, validator=validator, propertyType=propertyType, propertyTypeValue=propertyTypeValue, maxAllowed=maxAllowed)
