from core.agility.v3_3.agilitymodel.base.ScriptPropertyReference import ScriptPropertyReferenceBase
from core.agility.v3_3.agilitymodel.actions.ScriptPropertyReference import ScriptPropertyReferenceActions

class ScriptPropertyReference(ScriptPropertyReferenceBase, ScriptPropertyReferenceActions):
    '''
    classdocs
    '''
    def __init__(self, propertydefinition=None, type=[]):
        '''
        Constructor
        @param propertydefinition: propertydefinition minOccurs=0
        @type propertydefinition: Link
        @param type: type minOccurs=0 maxOccurs=unbounded
        @type type: Link
        '''
        ScriptPropertyReferenceBase.__init__(self, propertydefinition=propertydefinition, type=type)
