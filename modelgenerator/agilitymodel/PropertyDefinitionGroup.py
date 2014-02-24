from base.PropertyDefinitionGroup import PropertyDefinitionGroupBase
from actions.PropertyDefinitionGroup import PropertyDefinitionGroupActions

class PropertyDefinitionGroup(PropertyDefinitionGroupBase, PropertyDefinitionGroupActions):
    '''
    classdocs
    '''
    def __init__(self, derivedGroup=list(), displayName=None, parent=None, propertyDefinition=list()):
        '''
        Constructor
        @param derivedGroup: derivedGroup minOccurs=0 maxOccurs=unbounded
        @type derivedGroup: Link
        @param displayName: displayName minOccurs=0
        @type displayName: string
        @param parent: parent minOccurs=0
        @type parent: Link
        @param propertyDefinition: propertyDefinition minOccurs=0 maxOccurs=unbounded
        @type propertyDefinition: PropertyDefinition
        '''
        PropertyDefinitionGroupBase.__init__(self, derivedGroup=derivedGroup, displayName=displayName, parent=parent, propertyDefinition=propertyDefinition)
