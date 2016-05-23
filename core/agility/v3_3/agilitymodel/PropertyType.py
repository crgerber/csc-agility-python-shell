from core.agility.v3_3.agilitymodel.base.PropertyType import PropertyTypeBase
from core.agility.v3_3.agilitymodel.actions.PropertyType import PropertyTypeActions

class PropertyType(PropertyTypeBase, PropertyTypeActions):
    '''
    classdocs
    '''
    def __init__(self, valueprovider=None, displayname=None, valueconstraint=None, allowedassettype=None, rootvalue=[], owned=False, open=False, type=None):
        '''
        Constructor
        @param valueprovider: valueprovider minOccurs=0
        @type valueprovider: string
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param valueconstraint: valueconstraint minOccurs=0
        @type valueconstraint: ValueConstraintType
        @param allowedassettype: allowedassettype minOccurs=0
        @type allowedassettype: Link
        @param rootvalue: rootvalue minOccurs=0 maxOccurs=unbounded
        @type rootvalue: PropertyTypeValue
        @param owned: owned
        @type owned: boolean
        @param open: open
        @type open: boolean
        @param type: type minOccurs=0
        @type type: PrimitiveType
        '''
        PropertyTypeBase.__init__(self, valueprovider=valueprovider, displayname=displayname, valueconstraint=valueconstraint, allowedassettype=allowedassettype, rootvalue=rootvalue, owned=owned, open=open, type=type)
