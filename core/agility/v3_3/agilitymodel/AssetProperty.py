from core.agility.v3_3.agilitymodel.base.AssetProperty import AssetPropertyBase
from core.agility.v3_3.agilitymodel.actions.AssetProperty import AssetPropertyActions

class AssetProperty(AssetPropertyBase, AssetPropertyActions):
    '''
    classdocs
    '''
    def __init__(self, booleanvalue=None, overridable=False, floatvalue=None, propertytype=None, datevalue=None, id=None, intvalue=None, encrypted=False, description='', stringvalue=None, bytevalue=None, name=None, propertydefinition=None):
        '''
        Constructor
        @param booleanvalue: booleanvalue minOccurs=0
        @type booleanvalue: boolean
        @param overridable: overridable
        @type overridable: boolean
        @param floatvalue: floatvalue minOccurs=0
        @type floatvalue: decimal
        @param propertytype: propertytype minOccurs=0
        @type propertytype: Link
        @param datevalue: datevalue minOccurs=0
        @type datevalue: date
        @param id: id minOccurs=0
        @type id: int
        @param intvalue: intvalue minOccurs=0
        @type intvalue: int
        @param encrypted: encrypted
        @type encrypted: boolean
        @param description: description
        @type description: string
        @param stringvalue: stringvalue minOccurs=0
        @type stringvalue: string
        @param bytevalue: bytevalue minOccurs=0
        @type bytevalue: hexBinary
        @param name: name minOccurs=0
        @type name: string
        @param propertydefinition: propertydefinition minOccurs=0
        @type propertydefinition: Baselink
        '''
        AssetPropertyBase.__init__(self, booleanvalue=booleanvalue, overridable=overridable, floatvalue=floatvalue, propertytype=propertytype, datevalue=datevalue, id=id, intvalue=intvalue, encrypted=encrypted, description=description, stringvalue=stringvalue, bytevalue=bytevalue, name=name, propertydefinition=propertydefinition)
