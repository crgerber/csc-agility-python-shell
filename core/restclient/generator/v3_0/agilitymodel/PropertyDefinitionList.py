from base.PropertyDefinitionList import PropertyDefinitionListBase
from actions.PropertyDefinitionList import PropertyDefinitionListActions

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
