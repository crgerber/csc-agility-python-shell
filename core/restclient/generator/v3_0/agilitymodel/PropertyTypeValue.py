from .base.PropertyTypeValue import PropertyTypeValueBase
from .actions.PropertyTypeValue import PropertyTypeValueActions

class PropertyTypeValue(PropertyTypeValueBase, PropertyTypeValueActions):
    '''
    classdocs
    '''
    def __init__(self, displayname=None, parent=None, value=None, child=[]):
        '''
        Constructor
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param parent: parent minOccurs=0
        @type parent: Link
        @param value: value minOccurs=0
        @type value: string
        @param child: child minOccurs=0 maxOccurs=unbounded
        @type child: PropertyTypeValue
        '''
        PropertyTypeValueBase.__init__(self, displayname=displayname, parent=parent, value=value, child=child)
