from core.agility.v3_0.agilitymodel.base.ScriptPropertyReference import ScriptPropertyReferenceBase
from core.agility.v3_0.agilitymodel.actions.ScriptPropertyReference import ScriptPropertyReferenceActions

class ScriptPropertyReference(ScriptPropertyReferenceBase, ScriptPropertyReferenceActions):
    '''
    classdocs
    '''
    def __init__(self, type=[], propertydefinition=None):
        '''
        Constructor
        @param type: type minOccurs=0 maxOccurs=unbounded
        @type type: Link
        @param propertydefinition: propertydefinition minOccurs=0
        @type propertydefinition: Link
        '''
        ScriptPropertyReferenceBase.__init__(self, type=type, propertydefinition=propertydefinition)
