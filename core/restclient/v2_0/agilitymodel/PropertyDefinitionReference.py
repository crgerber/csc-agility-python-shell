from core.restclient.v2_0.agilitymodel.base.PropertyDefinitionReference import PropertyDefinitionReferenceBase
from core.restclient.v2_0.agilitymodel.actions.PropertyDefinitionReference import PropertyDefinitionReferenceActions

class PropertyDefinitionReference(PropertyDefinitionReferenceBase, PropertyDefinitionReferenceActions):
    '''
    classdocs
    '''
    def __init__(self, path=None, displayName=None, propertyDefinition=None):
        '''
        Constructor
        @param path: path minOccurs=0
        @type path: string
        @param displayName: displayName minOccurs=0
        @type displayName: string
        @param propertyDefinition: propertyDefinition minOccurs=0
        @type propertyDefinition: Link
        '''
        PropertyDefinitionReferenceBase.__init__(self, path=path, displayName=displayName, propertyDefinition=propertyDefinition)
