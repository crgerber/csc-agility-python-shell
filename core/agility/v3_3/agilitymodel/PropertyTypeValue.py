from core.agility.v3_3.agilitymodel.base.PropertyTypeValue import PropertyTypeValueBase
from core.agility.v3_3.agilitymodel.actions.PropertyTypeValue import PropertyTypeValueActions

class PropertyTypeValue(PropertyTypeValueBase, PropertyTypeValueActions):
    '''
    classdocs
    '''
    def __init__(self, costvalue=None, parent=None, value=None, displayname=None, child=[]):
        '''
        Constructor
        @param costvalue: costvalue minOccurs=0
        @type costvalue: CostValue
        @param parent: parent minOccurs=0
        @type parent: Link
        @param value: value minOccurs=0
        @type value: string
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param child: child minOccurs=0 maxOccurs=unbounded
        @type child: PropertyTypeValue
        '''
        PropertyTypeValueBase.__init__(self, costvalue=costvalue, parent=parent, value=value, displayname=displayname, child=child)
