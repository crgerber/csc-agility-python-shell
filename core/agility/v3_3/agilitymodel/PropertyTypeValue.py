from core.agility.v3_3.agilitymodel.base.PropertyTypeValue import PropertyTypeValueBase
from core.agility.v3_3.agilitymodel.actions.PropertyTypeValue import PropertyTypeValueActions

class PropertyTypeValue(PropertyTypeValueBase, PropertyTypeValueActions):
    '''
    classdocs
    '''
    def __init__(self, child=[], displayname=None, parent=None, value=None, costvalue=None):
        '''
        Constructor
        @param child: child minOccurs=0 maxOccurs=unbounded
        @type child: PropertyTypeValue
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param parent: parent minOccurs=0
        @type parent: Link
        @param value: value minOccurs=0
        @type value: string
        @param costvalue: costvalue minOccurs=0
        @type costvalue: CostValue
        '''
        PropertyTypeValueBase.__init__(self, child=child, displayname=displayname, parent=parent, value=value, costvalue=costvalue)
