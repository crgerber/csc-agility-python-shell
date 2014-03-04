from core.restclient.v2_0.agilitymodel.base.AssetProperty import AssetPropertyBase
from core.restclient.v2_0.agilitymodel.actions.AssetProperty import AssetPropertyActions

class AssetProperty(AssetPropertyBase, AssetPropertyActions):
    '''
    classdocs
    '''
    def __init__(self, description='', propertyDefinition=None, encrypted=False, floatValue=None, overridable=False, intValue=None, dateValue=None, propertyType=None, byteValue=None, stringValue=None, booleanValue=None, id=None, name=None):
        '''
        Constructor
        @param description: description
        @type description: string
        @param propertyDefinition: propertyDefinition minOccurs=0
        @type propertyDefinition: Link
        @param encrypted: encrypted
        @type encrypted: boolean
        @param floatValue: floatValue minOccurs=0
        @type floatValue: decimal
        @param overridable: overridable
        @type overridable: boolean
        @param intValue: intValue minOccurs=0
        @type intValue: int
        @param dateValue: dateValue minOccurs=0
        @type dateValue: date
        @param propertyType: propertyType minOccurs=0
        @type propertyType: Link
        @param byteValue: byteValue minOccurs=0
        @type byteValue: hexBinary
        @param stringValue: stringValue minOccurs=0
        @type stringValue: string
        @param booleanValue: booleanValue minOccurs=0
        @type booleanValue: boolean
        @param id: id minOccurs=0
        @type id: int
        @param name: name minOccurs=0
        @type name: string
        '''
        AssetPropertyBase.__init__(self, description=description, propertyDefinition=propertyDefinition, encrypted=encrypted, floatValue=floatValue, overridable=overridable, intValue=intValue, dateValue=dateValue, propertyType=propertyType, byteValue=byteValue, stringValue=stringValue, booleanValue=booleanValue, id=id, name=name)
