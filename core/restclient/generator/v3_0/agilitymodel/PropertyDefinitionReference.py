from .base.PropertyDefinitionReference import PropertyDefinitionReferenceBase
from .actions.PropertyDefinitionReference import PropertyDefinitionReferenceActions

class PropertyDefinitionReference(PropertyDefinitionReferenceBase, PropertyDefinitionReferenceActions):
    '''
    classdocs
    '''
    def __init__(self, path=None, displayname=None, propertydefinition=None):
        '''
        Constructor
        @param path: path minOccurs=0
        @type path: string
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param propertydefinition: propertydefinition minOccurs=0
        @type propertydefinition: Link
        '''
        PropertyDefinitionReferenceBase.__init__(self, path=path, displayname=displayname, propertydefinition=propertydefinition)
