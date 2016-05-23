from core.agility.v3_3.agilitymodel.base.PropertyTypeValue import PropertyTypeValueBase
from core.agility.v3_3.agilitymodel.actions.PropertyTypeValue import PropertyTypeValueActions

class PropertyTypeValue(PropertyTypeValueBase, PropertyTypeValueActions):
    '''
    classdocs
    '''
    def __init__(self, value=None, displayname=None, child=[], parent=None, costvalue=None):
        '''
        Constructor
        @param value: value minOccurs=0
        @type value: string
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param child: child minOccurs=0 maxOccurs=unbounded
        @type child: PropertyTypeValue
        @param parent: parent minOccurs=0
        @type parent: Link
        @param costvalue: costvalue minOccurs=0
        @type costvalue: CostValue
        '''
        PropertyTypeValueBase.__init__(self, value=value, displayname=displayname, child=child, parent=parent, costvalue=costvalue)
