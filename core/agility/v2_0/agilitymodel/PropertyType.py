from core.agility.v2_0.agilitymodel.base.PropertyType import PropertyTypeBase
from core.agility.v2_0.agilitymodel.actions.PropertyType import PropertyTypeActions

class PropertyType(PropertyTypeBase, PropertyTypeActions):
    '''
    classdocs
    '''
    def __init__(self, displayName=None, open=False, rootValue=list(), owned=False, valueProvider=None, type=None, valueConstraint=None):
        '''
        Constructor
        @param displayName: displayName minOccurs=0
        @type displayName: string
        @param open: open
        @type open: boolean
        @param rootValue: rootValue minOccurs=0 maxOccurs=unbounded
        @type rootValue: PropertyTypeValue
        @param owned: owned
        @type owned: boolean
        @param valueProvider: valueProvider minOccurs=0
        @type valueProvider: Link
        @param type: type minOccurs=0
        @type type: PrimitiveType
        @param valueConstraint: valueConstraint minOccurs=0
        @type valueConstraint: ValueConstraintType
        '''
        PropertyTypeBase.__init__(self, displayName=displayName, open=open, rootValue=rootValue, owned=owned, valueProvider=valueProvider, type=type, valueConstraint=valueConstraint)
