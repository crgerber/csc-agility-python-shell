from core.agility.v3_3.agilitymodel.base.PropertyDefinitionGroup import PropertyDefinitionGroupBase
from core.agility.v3_3.agilitymodel.actions.PropertyDefinitionGroup import PropertyDefinitionGroupActions

class PropertyDefinitionGroup(PropertyDefinitionGroupBase, PropertyDefinitionGroupActions):
    '''
    classdocs
    '''
    def __init__(self, derivedgroup=[], displayname=None, propertydefinition=[], parent=None):
        '''
        Constructor
        @param derivedgroup: derivedgroup minOccurs=0 maxOccurs=unbounded
        @type derivedgroup: Link
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param propertydefinition: propertydefinition minOccurs=0 maxOccurs=unbounded
        @type propertydefinition: PropertyDefinition
        @param parent: parent minOccurs=0
        @type parent: Link
        '''
        PropertyDefinitionGroupBase.__init__(self, derivedgroup=derivedgroup, displayname=displayname, propertydefinition=propertydefinition, parent=parent)
