from core.restclient.v2_0.agilitymodel.base.PropertyDefinitionList import PropertyDefinitionListBase
from core.restclient.v2_0.agilitymodel.actions.PropertyDefinitionList import PropertyDefinitionListActions

class PropertyDefinitionList(PropertyDefinitionListBase, PropertyDefinitionListActions):
    '''
    classdocs
    '''
    def __init__(self, definition=list()):
        '''
        Constructor
        @param definition: definition minOccurs=0 maxOccurs=unbounded
        @type definition: PropertyDefinition
        '''
        PropertyDefinitionListBase.__init__(self, definition=definition)
