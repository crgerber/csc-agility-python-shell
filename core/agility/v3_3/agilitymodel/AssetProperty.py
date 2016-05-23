from core.agility.v3_3.agilitymodel.base.AssetProperty import AssetPropertyBase
from core.agility.v3_3.agilitymodel.actions.AssetProperty import AssetPropertyActions

class AssetProperty(AssetPropertyBase, AssetPropertyActions):
    '''
    classdocs
    '''
    def __init__(self, datevalue=None, overridable=False, booleanvalue=None, name=None, intvalue=None, encrypted=False, description='', propertytype=None, stringvalue=None, bytevalue=None, id=None, propertydefinition=None, floatvalue=None):
        '''
        Constructor
        @param datevalue: datevalue minOccurs=0
        @type datevalue: date
        @param overridable: overridable
        @type overridable: boolean
        @param booleanvalue: booleanvalue minOccurs=0
        @type booleanvalue: boolean
        @param name: name minOccurs=0
        @type name: string
        @param intvalue: intvalue minOccurs=0
        @type intvalue: int
        @param encrypted: encrypted
        @type encrypted: boolean
        @param description: description
        @type description: string
        @param propertytype: propertytype minOccurs=0
        @type propertytype: Link
        @param stringvalue: stringvalue minOccurs=0
        @type stringvalue: string
        @param bytevalue: bytevalue minOccurs=0
        @type bytevalue: hexBinary
        @param id: id minOccurs=0
        @type id: int
        @param propertydefinition: propertydefinition minOccurs=0
        @type propertydefinition: Baselink
        @param floatvalue: floatvalue minOccurs=0
        @type floatvalue: decimal
        '''
        AssetPropertyBase.__init__(self, datevalue=datevalue, overridable=overridable, booleanvalue=booleanvalue, name=name, intvalue=intvalue, encrypted=encrypted, description=description, propertytype=propertytype, stringvalue=stringvalue, bytevalue=bytevalue, id=id, propertydefinition=propertydefinition, floatvalue=floatvalue)
