from base.PropertyType import PropertyTypeBase
from actions.PropertyType import PropertyTypeActions

class PropertyType(PropertyTypeBase, PropertyTypeActions):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, allowedassettype=None, open=False, rootvalue=[], owned=False, valueprovider=None, type=None, valueconstraint=None):
        '''
        Constructor
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param allowedassettype: allowedassettype minOccurs=0
        @type allowedassettype: Link
        @param open: open
        @type open: boolean
        @param rootvalue: rootvalue minOccurs=0 maxOccurs=unbounded
        @type rootvalue: PropertyTypeValue
        @param owned: owned
        @type owned: boolean
        @param valueprovider: valueprovider minOccurs=0
        @type valueprovider: string
        @param type: type minOccurs=0
        @type type: PrimitiveType
        @param valueconstraint: valueconstraint minOccurs=0
        @type valueconstraint: ValueConstraintType
        '''
        PropertyTypeBase.__init__(self, displayname=displayname, allowedassettype=allowedassettype, open=open, rootvalue=rootvalue, owned=owned, valueprovider=valueprovider, type=type, valueconstraint=valueconstraint)
