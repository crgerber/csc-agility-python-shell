from core.agility.v3_3.agilitymodel.base.PropertyDefinitionGroup import PropertyDefinitionGroupBase
from core.agility.v3_3.agilitymodel.actions.PropertyDefinitionGroup import PropertyDefinitionGroupActions

class PropertyDefinitionGroup(PropertyDefinitionGroupBase, PropertyDefinitionGroupActions):
    '''
    classdocs
    '''
    def __init__(self, parent=None, displayname=None, derivedgroup=[], propertydefinition=[]):
        '''
        Constructor
        @param parent: parent minOccurs=0
        @type parent: Link
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param derivedgroup: derivedgroup minOccurs=0 maxOccurs=unbounded
        @type derivedgroup: Link
        @param propertydefinition: propertydefinition minOccurs=0 maxOccurs=unbounded
        @type propertydefinition: PropertyDefinition
        '''
        PropertyDefinitionGroupBase.__init__(self, parent=parent, displayname=displayname, derivedgroup=derivedgroup, propertydefinition=propertydefinition)
