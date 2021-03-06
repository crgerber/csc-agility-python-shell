from core.agility.v2_0.agilitymodel.base.ScriptPropertyReference import ScriptPropertyReferenceBase
from core.agility.v2_0.agilitymodel.actions.ScriptPropertyReference import ScriptPropertyReferenceActions

class ScriptPropertyReference(ScriptPropertyReferenceBase, ScriptPropertyReferenceActions):
    '''
    classdocs
    '''
    def __init__(self, type=list(), propertyDefinition=None):
        '''
        Constructor
        @param type: type minOccurs=0 maxOccurs=unbounded
        @type type: Link
        @param propertyDefinition: propertyDefinition minOccurs=0
        @type propertyDefinition: Link
        '''
        ScriptPropertyReferenceBase.__init__(self, type=type, propertyDefinition=propertyDefinition)
