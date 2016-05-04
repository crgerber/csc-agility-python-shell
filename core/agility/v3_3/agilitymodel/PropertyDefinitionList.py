from core.agility.v3_3.agilitymodel.base.PropertyDefinitionList import PropertyDefinitionListBase
from core.agility.v3_3.agilitymodel.actions.PropertyDefinitionList import PropertyDefinitionListActions

class PropertyDefinitionList(PropertyDefinitionListBase, PropertyDefinitionListActions):
    '''
    classdocs
    '''
    def __init__(self, definition=[]):
        '''
        Constructor
        @param definition: definition minOccurs=0 maxOccurs=unbounded
        @type definition: PropertyDefinition
        '''
        PropertyDefinitionListBase.__init__(self, definition=definition)
