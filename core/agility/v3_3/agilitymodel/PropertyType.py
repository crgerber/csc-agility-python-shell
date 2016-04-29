from core.agility.v3_3.agilitymodel.base.PropertyType import PropertyTypeBase
from core.agility.v3_3.agilitymodel.actions.PropertyType import PropertyTypeActions

class PropertyType(PropertyTypeBase, PropertyTypeActions):
    '''
    classdocs
    '''
    def __init__(self, valueprovider=None, rootvalue=[], open=False, valueconstraint=None, allowedassettype=None, owned=False, displayname=None, type=None):
        '''
        Constructor
        @param valueprovider: valueprovider minOccurs=0
        @type valueprovider: string
        @param rootvalue: rootvalue minOccurs=0 maxOccurs=unbounded
        @type rootvalue: PropertyTypeValue
        @param open: open
        @type open: boolean
        @param valueconstraint: valueconstraint minOccurs=0
        @type valueconstraint: ValueConstraintType
        @param allowedassettype: allowedassettype minOccurs=0
        @type allowedassettype: Link
        @param owned: owned
        @type owned: boolean
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param type: type minOccurs=0
        @type type: PrimitiveType
        '''
        PropertyTypeBase.__init__(self, valueprovider=valueprovider, rootvalue=rootvalue, open=open, valueconstraint=valueconstraint, allowedassettype=allowedassettype, owned=owned, displayname=displayname, type=type)
