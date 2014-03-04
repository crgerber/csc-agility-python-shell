from core.restclient.v2_0.agilitymodel.base.PropertyTypeValue import PropertyTypeValueBase
from core.restclient.v2_0.agilitymodel.actions.PropertyTypeValue import PropertyTypeValueActions

class PropertyTypeValue(PropertyTypeValueBase, PropertyTypeValueActions):
    '''
    classdocs
    '''
    def __init__(self, displayName=None, parent=None, value=None, child=list()):
        '''
        Constructor
        @param displayName: displayName minOccurs=0
        @type displayName: string
        @param parent: parent minOccurs=0
        @type parent: Link
        @param value: value minOccurs=0
        @type value: string
        @param child: child minOccurs=0 maxOccurs=unbounded
        @type child: PropertyTypeValue
        '''
        PropertyTypeValueBase.__init__(self, displayName=displayName, parent=parent, value=value, child=child)
