from .base.AssetProperty import AssetPropertyBase
from .actions.AssetProperty import AssetPropertyActions

class AssetProperty(AssetPropertyBase, AssetPropertyActions):
    '''
    classdocs
    '''
    def __init__(self, description='', propertydefinition=None, encrypted=False, floatvalue=None, overridable=False, intvalue=None, datevalue=None, propertytype=None, bytevalue=None, stringvalue=None, booleanvalue=None, id=None, name=None):
        '''
        Constructor
        @param description: description
        @type description: string
        @param propertydefinition: propertydefinition minOccurs=0
        @type propertydefinition: Link
        @param encrypted: encrypted
        @type encrypted: boolean
        @param floatvalue: floatvalue minOccurs=0
        @type floatvalue: decimal
        @param overridable: overridable
        @type overridable: boolean
        @param intvalue: intvalue minOccurs=0
        @type intvalue: int
        @param datevalue: datevalue minOccurs=0
        @type datevalue: date
        @param propertytype: propertytype minOccurs=0
        @type propertytype: Link
        @param bytevalue: bytevalue minOccurs=0
        @type bytevalue: hexBinary
        @param stringvalue: stringvalue minOccurs=0
        @type stringvalue: string
        @param booleanvalue: booleanvalue minOccurs=0
        @type booleanvalue: boolean
        @param id: id minOccurs=0
        @type id: int
        @param name: name minOccurs=0
        @type name: string
        '''
        AssetPropertyBase.__init__(self, description=description, propertydefinition=propertydefinition, encrypted=encrypted, floatvalue=floatvalue, overridable=overridable, intvalue=intvalue, datevalue=datevalue, propertytype=propertytype, bytevalue=bytevalue, stringvalue=stringvalue, booleanvalue=booleanvalue, id=id, name=name)
